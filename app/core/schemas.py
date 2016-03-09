from marshmallow_jsonapi import fields
from app.framework.schema import BaseSchema
from entities import Notebook, Note, NoteReference


class NotebookSchema(BaseSchema):
    id = fields.Str(dump_only=True)
    slug = fields.Str(required=False)

    notes = fields.Relationship(
        self_url='/notebooks/{notebook_id}/notes',
        self_url_kwargs={'notebook_id': '<id>'}
    )

    class Meta:
        entity = Notebook


class NoteSchema(BaseSchema):
    id = fields.Str(dump_only=True)
    resume = fields.Str(required=True)
    contents = fields.Str(required=True)

    notebook = fields.Relationship(
        self_url='/notebook/{id}',
        self_url_kwargs={'id': '<id>'}
    )

    class Meta:
        entity = Note


class NoteReferenceSchema(BaseSchema):
    id = fields.Str(dump_only=True)
    resume = fields.Str(required=True)

    class Meta:
        entity = NoteReference
        type_ = 'notes'
