from llexer import LLexer
from ltoken import LToken

# Context-free grammar G for L is:
# Statements -> Statement ; Statements | end
# Statement -> id = Expr | print id
# Expr- > Term | Term + Expr | Term – Expr
# Term -> Factor | Factor * Term
# Factor -> int | id | ( Expr )

class LParser():
    def __init__(self):
        self.stack = []
        self.lexer = LLexer()
        self.curr_token = LToken("",LToken.ERROR)

    def parse(self):
        self.next_token() 
        self.statements()
        print()
        # Make sure the intermediate code ends with a newline
    
    def error(self):
        print("SYNTAX ERROR")
        exit(1)
    
    def next_token(self): 
        self.curr_token = self.lexer.get_next_token()
        if self.curr_token.token_code == LToken.ERROR: 
            self.error()

    def statements(self):
        if self.curr_token.token_code == LToken.ID or self.curr_token.token_code == LToken.PRINT:
            self.statement()
            if self.curr_token.token_code == LToken.SEMICOL:
                self.next_token()
                self.statements()
            else:
                self.error()
        elif self.curr_token.token_code == LToken.END:
            return
        else:
            self.error()
