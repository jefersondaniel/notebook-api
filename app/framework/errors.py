from flask import jsonify
from app import app
from mongoengine.errors import NotUniqueError, DoesNotExist
from mongoengine.errors import ValidationError as MongoValidationError
from marshmallow import ValidationError
from marshmallow_jsonapi.exceptions import IncorrectTypeError


@app.errorhandler(404)
def make_not_found_error_output(error):
    return make_simple_error_output(
        'The requested Resource was not found on the server. If you entered the URL manually please check your spelling and try again.',
        404
    )


def make_marshmallow_error_output(e, status_code=400):
    return make_error_output(e.messages['errors'], status_code)


def make_exception_error_output(e, status_code=500):
    return make_simple_error_output(
        parse_error_message(e.message),
        status_code
    )


def make_simple_error_output(message, status_code):
    return make_error_output(
        [
            {
                'detail': message
            }
        ],
        status_code
    )


def make_error_output(errors, status_code):
    if not errors:
        errors = []

    for error in errors:
        if 'status' not in error:
            error['status'] = status_code

    response = jsonify({'errors': errors})
    response.status_code = status_code
    return response


def parse_error_message(message):
    replacements = {
        u'not a valid ObjectId': 'Invalid id',
    }

    for key in replacements:
        if key in message:
            message = replacements[key]

    return message


def handle_exception(error):
    if isinstance(error, ValidationError) or\
            isinstance(error, IncorrectTypeError):
        return make_marshmallow_error_output(error, 400)
    elif isinstance(error, MongoValidationError):
        return make_exception_error_output(error, 400)
    elif isinstance(error, DoesNotExist):
        return make_not_found_error_output(error)
    elif isinstance(error, NotUniqueError):
        return make_exception_error_output(error, 400)
    else:
        return make_exception_error_output(error, 500)
