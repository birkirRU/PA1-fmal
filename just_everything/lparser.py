from llexer import LLexer
from ltoken import LToken
import sys

# Context-free grammar G for L is:
# Statements -> Statement ; Statements | end
# Statement -> id = Expr | print id
# Expr- > Term | Term + Expr | Term – Expr
# Term -> Factor | Factor * Term
# Factor -> int | id | ( Expr )

class LParser():
    def __init__(self, lexer: LLexer):
        # self.stack = []
        self.lexer = lexer
        self.curr_token = LToken('', LToken.ERROR)

    def parse(self):
        self.next_token() 
        self.statements()
        print()
        # Make sure the intermediate code ends with a newline
    
    def error(self):
        print("Syntax error")
        sys.exit(0)
    
    def next_token(self): 
        self.curr_token = self.lexer.get_next_token()
        if self.curr_token.token_code == LToken.ERROR: 
            self.error()

    def statements(self):
        if self.curr_token.token_code == LToken.ID:
            print(f"PUSH {self.curr_token.lexeme}")
            self.next_token()
            self.statement()
            if self.curr_token.token_code == LToken.SEMICOL:
                self.next_token()
                self.statements()
            else:
                self.error()

        elif self.curr_token.token_code == LToken.PRINT:
            self.next_token()
            if self.curr_token.token_code == LToken.ID:
                print(f"PUSH {self.curr_token.lexeme}")
                print("PRINT")
            else:
                self.error()
            self.next_token()
            if self.curr_token.token_code == LToken.SEMICOL:
                self.next_token()
                self.statements()
            else:
                self.error()
        elif self.curr_token.token_code == LToken.END:
            return
        else:
            self.error()
    
    def statement(self):
        if self.curr_token.token_code == LToken.ASSIGN:
            self.expr()
            print("ASSIGN")
            # print(f"PUSH {self.curr_token.lexeme}")
        elif self.curr_token.token_code == LToken.PRINT:
            print("PRINT")
        else:
            self.error()
    
    def expr(self):
        self.term()
        if self.curr_token.token_code == LToken.PLUS:
            self.expr()
            print("ADD")
        elif self.curr_token.token_code == LToken.MINUS:
            self.expr()
            print("SUB")

    def term(self):
        self.next_token()
        self.factor()
        if self.curr_token.token_code == LToken.MULT:
            self.term()
            print("MULT")
    
    def factor(self):
        if self.curr_token.token_code == LToken.INT:
            print(f"PUSH {self.curr_token.lexeme}")
            self.next_token()

        elif self.curr_token.token_code == LToken.ID:
            print(f"PUSH {self.curr_token.lexeme}")
            self.next_token()

        elif self.curr_token.token_code == LToken.LPAREN:
            self.expr()
            if self.curr_token.token_code == LToken.RPAREN:
                self.next_token()
        else:
            self.error()