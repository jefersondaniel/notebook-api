import inflect
from flask import request
from flask_restful.utils import unpack
from marshmallow import post_load
from marshmallow_jsonapi import Schema, SchemaOpts, fields
from app.framework.errors import make_marshmallow_error_output,\
    make_simple_error_output


inflect_engine = inflect.engine()


class ReferenceField(fields.Field):
    def __init__(self, entity, *args, **kwargs):
        self.entity = entity
        fields.Field.__init__(self, *args, **kwargs)

    def _serialize(self, value, attr, obj):
        if value is None:
            return ''
        return value.id

    def _deserialize(self, value, attr, obj):
        result = self.entity.objects.get(id=str(value))
        return result


class BaseSchemaOpts(SchemaOpts):
    def __init__(self, meta):
        self.envelope_key = 'data'
        self.entity = getattr(meta, 'entity')
        if (self.entity and not hasattr(meta, 'type_')):
            setattr(
                meta,
                'type_',
                inflect_engine.plural(self.entity.__name__).lower()
            )
        SchemaOpts.__init__(self, meta)


class BaseSchema(Schema):
    OPTIONS_CLASS = BaseSchemaOpts

    def __init__(self, *args, **kwargs):
        self.transform_entity = kwargs.pop('transform_entity', True)
        Schema.__init__(self, *args, **kwargs)

    @post_load
    def parse(self, data):
        if self.transform_entity:
            return self.opts.entity(**data)
        else:
            return data

    class Meta:
        entity = None
        strict = True


def input_schema(schema):
    def upper_wrapper(fn):
        def inner_wrapper(self, *args, **kwargs):
            request_data = request.get_json()
            if not request_data:
                return make_simple_error_output(
                    'Request body must be a valid JSON',
                    415
                )
            data, err = schema.load(request_data)
            if err:
                return make_marshmallow_error_output(err)
            return fn(self, data, *args, **kwargs)
        return inner_wrapper
    return upper_wrapper


def output_schema(schema):
    def upper_wrapper(fn):
        def inner_wrapper(self, *args, **kwargs):
            resp = fn(self, *args, **kwargs)

            if isinstance(resp, tuple):
                data, code, headers = unpack(resp)
                return schema.dump(data)[0], code, headers
            else:
                return schema.dump(resp)[0]

        return inner_wrapper
    return upper_wrapper
