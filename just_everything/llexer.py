import sys
from ltoken import LToken

class LLexer:
    def __init__(self):
        self.current_character = None

    def skip_whitespace(self):
        whitespace_chars = {" ", "\t", "\n"}
        while self.current_character in whitespace_chars:
            self.current_character = sys.stdin.read(1)
    
    def extract_identifier(self):
        accumulated = ""
        while self.current_character.isalpha():
            accumulated += self.current_character
            self.current_character = sys.stdin.read(1)
        
        keyword_map = {
            'print': LToken.PRINT,
            'end': LToken.END
        }
        
        token_type = keyword_map.get(accumulated, LToken.ID)
        return LToken(accumulated, token_type)
        
    def extract_number(self):
        accumulated = ""
        while self.current_character.isdigit():
            accumulated += self.current_character
            self.current_character = sys.stdin.read(1)
        return LToken(accumulated, LToken.INT)

    def get_next_token(self):
        if self.current_character is None:
            self.current_character = sys.stdin.read(1)
        
        self.skip_whitespace()
        
        operator_tokens = {
            "+": LToken.PLUS,
            "-": LToken.MINUS,
            "*": LToken.MULT,
            "(": LToken.LPAREN,
            ")": LToken.RPAREN,
            "=": LToken.ASSIGN,
            ";": LToken.SEMICOL
        }
        
        if self.current_character in operator_tokens:
            char_value = self.current_character
            self.current_character = None
            return LToken(char_value, operator_tokens[char_value])
        
        if self.current_character.isalpha():
            return self.extract_identifier()
        
        if self.current_character.isdigit():
            return self.extract_number()
        
        error_char = self.current_character
        self.current_character = None
        return LToken(error_char, LToken.ERROR)