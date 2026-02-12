import sys
from ltoken import LToken
from llexer import LLexer


class LParser:
    def __init__(self, lexer: LLexer):
        self.lexer = lexer
        self.curr_token = LToken('', LToken.ERROR)
    
    def error(self):
        print("Syntax error")
        sys.exit(0)
    
    def parse(self):
        self.next_token()
        self.statements()
        print()

    def next_token(self):
        self.curr_token = self.lexer.get_next_token()
        if self.curr_token.token_code == LToken.ERROR:
            self.error()

    # Statements -> Statement ; Statements | end
    def statements(self):
        if self.curr_token.token_code == LToken.END:
            return
        else:
            self.statement()
            if self.curr_token.token_code == LToken.SEMICOL:
                self.next_token()
                self.statements()
            else:
                self.error()

    # Statement -> id = Expr | print id
    def statement(self):
        if self.curr_token.token_code == LToken.ID:
            print(f"PUSH {self.curr_token.lexeme}")
            self.next_token()

            if self.curr_token.token_code == LToken.ASSIGN:
                self.next_token()
                self.expr()
                print("ASSIGN")

            else:
                self.error()
        elif self.curr_token.token_code == LToken.PRINT:
            self.next_token()
            print(f"PUSH {self.curr_token.lexeme}")
            print("PRINT")
            self.next_token()

        else:
            self.error()

    # Expr -> Term | Term + Expr | Term – Expr
    def expr(self):
        self.term()
        if self.curr_token.token_code == LToken.PLUS:
            self.next_token()
            self.expr()
            print("ADD")
        elif self.curr_token.token_code == LToken.MINUS:
            self.next_token()
            self.expr()
            print("SUB")

    # Term -> Factor | Factor * Term
    def term(self):
        self.factor()
        if self.curr_token.token_code == LToken.MULT:
            self.next_token()
            self.term()
            print("MULT")

    # Factor -> int | id | ( Expr )
    def factor(self):
        if self.curr_token.token_code == LToken.INT:
            print(f"PUSH {self.curr_token.lexeme}")
            self.next_token()

        elif self.curr_token.token_code == LToken.ID:
            print(f"PUSH {self.curr_token.lexeme}")
            self.next_token()

        elif self.curr_token.token_code == LToken.LPAREN:
            self.next_token()
            self.expr()

            if self.curr_token.token_code != LToken.RPAREN:
                self.error()
            else:
                self.next_token()
        else:
            self.error()
