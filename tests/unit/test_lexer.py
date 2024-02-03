import pytest
from src.lexer import Token, tokenize, JsonTokenType


@pytest.fixture
def data_file_path():
    return "tests/data/test_json.json"


def test_tokenize_strings(data_file_path):
    with open(data_file_path, encoding="utf-8") as f:
        data = f.read()
    tokens = tokenize(data)

    assert tokens == [
        Token(token_type=JsonTokenType.TOKEN_OPEN_OBJECT, value="{"),
        Token(token_type=JsonTokenType.TOKEN_DOUBLE_QUOTE, value='"'),
        Token(token_type=JsonTokenType.TOKEN_STRING_LITERAL, value="name"),
        Token(token_type=JsonTokenType.TOKEN_DOUBLE_QUOTE, value='"'),
        Token(token_type=JsonTokenType.TOKEN_COLON, value=":"),
        Token(token_type=JsonTokenType.TOKEN_DOUBLE_QUOTE, value='"'),
        Token(token_type=JsonTokenType.TOKEN_STRING_LITERAL, value="james"),
        Token(token_type=JsonTokenType.TOKEN_DOUBLE_QUOTE, value='"'),
        Token(token_type=JsonTokenType.TOKEN_CLOSE_OBJECT, value="}"),
    ]


@pytest.fixture
def number_data_filepath():
    return "tests/data/test_number.json"


def test_tokenize_numbers(number_data_filepath):
    with open(number_data_filepath, encoding="utf-8") as f:
        data = f.read()
    tokens = tokenize(data)
    assert tokens == [
        Token(JsonTokenType.TOKEN_OPEN_OBJECT, value="{"),
        Token(JsonTokenType.TOKEN_DOUBLE_QUOTE, value='"'),
        Token(JsonTokenType.TOKEN_STRING_LITERAL, value="a"),
        Token(JsonTokenType.TOKEN_DOUBLE_QUOTE, value='"'),
        Token(JsonTokenType.TOKEN_COLON, value=":"),
        Token(JsonTokenType.TOKEN_NUMBER, value="10"),
        Token(JsonTokenType.TOKEN_COMMA, value=","),
        Token(JsonTokenType.TOKEN_DOUBLE_QUOTE, value='"'),
        Token(JsonTokenType.TOKEN_STRING_LITERAL, value="b"),
        Token(JsonTokenType.TOKEN_DOUBLE_QUOTE, value='"'),
        Token(JsonTokenType.TOKEN_COLON, value=":"),
        Token(JsonTokenType.TOKEN_NUMBER, value="12"),
        Token(JsonTokenType.TOKEN_CLOSE_OBJECT, value="}"),
    ]


@pytest.fixture
def array_json_filepath():
    return "tests/data/test_array.json"


def test_tokenize_array(array_json_filepath):
    with open(array_json_filepath, encoding="utf-8") as f:
        data = f.read()
    tokens = tokenize(data)
    assert tokens == [
        Token(JsonTokenType.TOKEN_OPEN_OBJECT, value="{"),
        Token(JsonTokenType.TOKEN_DOUBLE_QUOTE, value='"'),
        Token(JsonTokenType.TOKEN_STRING_LITERAL, value="a"),
        Token(JsonTokenType.TOKEN_DOUBLE_QUOTE, value='"'),
        Token(JsonTokenType.TOKEN_COLON, value=":"),
        Token(JsonTokenType.TOKEN_OPEN_ARRAY, value="["),
        Token(JsonTokenType.TOKEN_NUMBER, value="1"),
        Token(JsonTokenType.TOKEN_COMMA, value=","),
        Token(JsonTokenType.TOKEN_NUMBER, value="2"),
        Token(JsonTokenType.TOKEN_COMMA, value=","),
        Token(JsonTokenType.TOKEN_NUMBER, value="3"),
        Token(JsonTokenType.TOKEN_CLOSE_ARRAY, value="]"),
        Token(JsonTokenType.TOKEN_CLOSE_OBJECT, value="}"),
    ]


@pytest.fixture
def floats_json_filepath():
    return "tests/data/test_floats.json"


def test_tokenize_floats(floats_json_filepath):
    with open(floats_json_filepath, encoding="utf-8") as f:
        data = f.read()
    tokens = tokenize(data)
    assert tokens == [
        Token(JsonTokenType.TOKEN_OPEN_OBJECT, value="{"),
        Token(JsonTokenType.TOKEN_DOUBLE_QUOTE,value='"'),
        Token(JsonTokenType.TOKEN_STRING_LITERAL,value='a'),
        Token(JsonTokenType.TOKEN_DOUBLE_QUOTE,value='"'),
        Token(JsonTokenType.TOKEN_COLON, value=':'),
        Token(JsonTokenType.TOKEN_NUMBER, value='1.05'),
        Token(JsonTokenType.TOKEN_CLOSE_OBJECT,value='}'),

    ]


@pytest.fixture
def neg_number_filepath():
    return "tests/data/test_neg_number.json"


def test_negative_number(neg_number_filepath):
    with open(neg_number_filepath, encoding="utf-8") as f:
        data = f.read()
    tokens = tokenize(data)
    assert tokens == [
        Token(JsonTokenType.TOKEN_OPEN_OBJECT, value="{"),
        Token(JsonTokenType.TOKEN_DOUBLE_QUOTE,value='"'),
        Token(JsonTokenType.TOKEN_STRING_LITERAL,value='a'),
        Token(JsonTokenType.TOKEN_DOUBLE_QUOTE,value='"'),
        Token(JsonTokenType.TOKEN_COLON, value=':'),
        Token(JsonTokenType.TOKEN_NUMBER, value='-5'),
        Token(JsonTokenType.TOKEN_CLOSE_OBJECT,value='}'),
    ]