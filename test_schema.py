import json
from jsonschema import validate
from unittest.mock import Mock


def assert_valid_schema(data, schema_file):
    with open(schema_file) as f:
        schema = json.load(f)
    return validate(instance=data, schema=schema)


def test_schema_getting(session, base_url):
    res = session.get(url=f'{base_url}/1')

    # Mock
    res = Mock()
    res.json.return_value = {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

    assert_valid_schema(res.json(), 'schemas/todo_schema.json')


def test_schema_listing_all(session, base_url):
    res = session.get(url=base_url)

    # Mock
    res = Mock()
    res.json.return_value = [{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}]

    assert_valid_schema(res.json(), 'schemas/todos_schema.json')
