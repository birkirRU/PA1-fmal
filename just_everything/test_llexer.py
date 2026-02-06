import sys
sys.path.insert(0, '../src')

from ltoken import LToken
from llexer import LLexer

if __name__ == "__main__":
    lexer = LLexer()
    curr_token = LToken("",LToken.ERROR)

    while curr_token.token_code != LToken.END:
        curr_token = lexer.get_next_token()
        print(curr_token)