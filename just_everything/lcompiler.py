from llexer import LLexer
from lparser import LParser


if __name__ == "__main__":
    lexer = LLexer()
    parser = LParser(lexer)
    try:
        parser.parse()
    except SyntaxError as e:
        pass