from behave import *
import requests
import os
import json
import re

HOST = os.environ.get('HOST', '127.0.0.1')
PORT = os.environ.get('PORT', 5000)


def get_url(endingpoint):
    return 'http://{}:{}{}'.format(HOST, PORT, endingpoint)


def compare_lists(expected_list, actual_list, key=None):
    assert type(expected_list) is list
    assert type(actual_list) is list

    for i, item in enumerate(expected_list):
        compare_values(item, actual_list[i], key=key)


def compare_dicts(expected_dict, actual_dict, key=None):
    assert type(expected_dict) is dict
    assert type(actual_dict) is dict

    for key in expected_dict:
        expected_value = expected_dict[key]
        actual_value = actual_dict.get(key, None)

        compare_values(expected_value, actual_value, key=key)


def compare_values(expected_value, actual_value, key=None):
    if type(expected_value) is dict:
        compare_dicts(expected_value, actual_value, key=key)
    elif type(expected_value) is list:
        compare_lists(expected_value, actual_value, key=key)
    elif isinstance(expected_value, basestring)\
            and expected_value[0] == '%'\
            and expected_value[-1] == '%':
        if not re.match(expected_value.strip('%'), actual_value or ''):
            raise AssertionError(
                'Expected {} to match regex {} at key {}'.format(
                    repr(actual_value),
                    repr(expected_value),
                    key
                )
            )
    else:
        try:
            assert expected_value == actual_value
        except AssertionError:
            raise AssertionError(
                'Expected {} to equal {} at key {}'.format(
                    repr(actual_value),
                    repr(expected_value),
                    key
                )
            )


def do_request(context, method, endingpoint, body=None):
    fn = getattr(requests, method.lower())
    kwargs = {}

    if hasattr(context, 'request_headers'):
        kwargs['headers'] = context.request_headers

    if body:
        kwargs['data'] = body

    context.response = fn(get_url(endingpoint), **kwargs)


@when(u'I set header "{}" with value "{}"')
def i_set_header_with_value(context, key, value):
    if not hasattr(context, 'request_headers'):
        context.request_headers = {}
    context.request_headers[key] = value


@when(u'I send a {} request to "{}" with body')
def i_send_a_request_with_body(context, method, endingpoint):
    do_request(context, method, endingpoint, context.text)


@when(u'I send a {} request to "{}"')
def i_send_a_get_request(context, method, endingpoint):
    do_request(context, method, endingpoint)


@then(u'the response should contain json')
def the_response_should_contain_json(context):
    expected_data = json.loads(context.text)
    actual_data = json.loads(context.response.text)
    compare_values(expected_data, actual_data)


@then(u'the response code should be {}')
def the_response_should_be(context, status_code):
    compare_values(int(status_code), context.response.status_code)


@then(u'print response')
def print_response(context):
    print(context.response.text)
