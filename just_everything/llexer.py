import sys
import unicodedata
from ltoken import LToken


class LLexer():
    def __init__(self):
        self.letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.digits = '0123456789'
        self.single_char_tokens = {
            '+': LToken.PLUS,
            '-': LToken.MINUS,
            '*': LToken.MULT,
            '(': LToken.LPAREN,
            ')': LToken.RPAREN,
            ';': LToken.SEMICOL,
            '=': LToken.ASSIGN
        }
        self.curr_char = self._next_char()


    def _next_char(self):
        """
        Returns '' for EOF
        Otherwise next charecter in stdin buffer
        """
        return sys.stdin.read(1)

    def get_next_token(self):

        if self.curr_char == '':
            return

        while self.curr_char.isspace():
            self.curr_char = self._next_char()
        
        if self.curr_char in self.single_char_tokens:
            token = LToken(self.curr_char, self.single_char_tokens[self.curr_char])
            self.curr_char = self._next_char()
            return token

        elif self.curr_char in self.letters:
            lexeme = self.curr_char
            while self.curr_char in self.letters and self.curr_char != '':
                next_char = self._next_char()
                self.curr_char = next_char
                lexeme += next_char if self.curr_char in self.letters else ''

            if lexeme == 'print':
                return LToken(lexeme, LToken.PRINT)
            elif lexeme == 'end':
                return LToken(lexeme, LToken.END)
            elif (not self.curr_char.isspace() and self.curr_char not in self.single_char_tokens):
                return LToken(f"LEXICAL {unicodedata.name(self.curr_char)} ERROR", LToken.ERROR)

            return LToken(lexeme, LToken.ID)
        
        elif self.curr_char in self.digits:
            lexeme = self.curr_char
            while self.curr_char in self.digits and self.curr_char != '':
                next_char = self._next_char()
                self.curr_char = next_char
                lexeme += next_char if self.curr_char in self.digits else ''
            
            if (not self.curr_char.isspace() and self.curr_char not in self.single_char_tokens):
                return LToken(f"LEXICAL {unicodedata.name(self.curr_char)} ERROR", LToken.ERROR)
            return LToken(lexeme, LToken.INT)
        
        else:
            return LToken(f"LEXICAL {unicodedata.name(self.curr_char)} ERROR", LToken.ERROR)

