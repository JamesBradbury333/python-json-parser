from enum import Enum
from dataclasses import dataclass
from typing import Union, List


def main():
    with open("tests/data/test_json.json") as f:
        source_code = f.read()
    print(source_code)
    for thing in tokenize(source_code):
        print(thing)


class JsonTokenType(Enum):
    # EOF Token
    TOKEN_END_OF_FILE = "EOF"
    # Illegal unknown character
    TOKEN_ILLEGAL = "Illegal Character"

    # Structural Characters in JSON
    TOKEN_OPEN_OBJECT = "open_object"
    TOKEN_CLOSE_OBJECT = "close_object"
    TOKEN_OPEN_ARRAY = "open_arrray"
    TOKEN_CLOSE_ARRAY = "close_array"
    TOKEN_COMMA = "comma"
    TOKEN_COLON = " colon"
    TOKEN_SEMI_COLON = "semi_colon"
    TOKEN_DOUBLE_QUOTE = "double_quote"

    # Data Types in Json
    TOKEN_STRING_LITERAL = "string_literal"
    TOKEN_NUMBER = "Number"
    TOKEN_BOOLEAN = "Boolean"
    TOKEN_NULL = "Null"
    


@dataclass
class Token:
    token_type: JsonTokenType
    value: Union[str, None]


def tokenize(source_code: str) -> List[Token]:
    tokens = []
    src = list(source_code)

    while len(src) > 0:
        print(src)
        if src[0] == "{":
            tokens.append(Token(JsonTokenType.TOKEN_OPEN_OBJECT, src.pop(0)))
        elif src[0] == "}":
            tokens.append(Token(JsonTokenType.TOKEN_CLOSE_OBJECT, src.pop(0)))
        elif src[0] == "[":
            tokens.append(Token(JsonTokenType.TOKEN_OPEN_ARRAY, src.pop(0)))
        elif src[0] == "]":
            tokens.append(Token(JsonTokenType.TOKEN_CLOSE_ARRAY, src.pop(0)))
        elif src[0] == ",":
            tokens.append(Token(JsonTokenType.TOKEN_COMMA, src.pop(0)))
        elif src[0] == ":":
            tokens.append(Token(JsonTokenType.TOKEN_COLON, src.pop(0)))
        elif src[0] == ";":
            tokens.append(Token(JsonTokenType.TOKEN_SEMI_COLON, src.pop(0)))
        elif src[0] == '"':
            tokens.append(Token(JsonTokenType.TOKEN_DOUBLE_QUOTE, src.pop(0)))

        elif src[0].isalpha():
            ident = ""
            while len(src) > 0 and src[0].isalpha():
                ident = f"{ident}{src.pop(0)}"
            tokens.append(Token(JsonTokenType.TOKEN_STRING_LITERAL, ident))
        elif src[0].isdigit() or src[0] == "-":
            num = ""
            while len(src) > 0 and (src[0].isdigit() or src[0]=="-" or src[0] == "."):
                num = f"{num}{src.pop(0)}"
            tokens.append(Token(JsonTokenType.TOKEN_NUMBER, num))
        elif src[0].isspace():
            src.pop(0)
        else:
            print(src[0])
            raise NotImplementedError("character not implemented")
    return tokens


if __name__ == "__main__":
    main()
