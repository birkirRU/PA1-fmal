# import sys
# sys.path.insert(0, '../src')


from src.llexer import LLexer
from src.lparser import LParser

if __name__ == "__main__":
    lexer = LLexer()
    parser = LParser(lexer)
    parser.parse()