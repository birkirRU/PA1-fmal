
class LToken():
    ID = 0 
    ASSIGN = 1
    SEMICOL = 2
    INT = 3
    PLUS = 4
    MINUS = 5
    MULT = 6
    LPAREN = 7
    RPAREN = 8
    PRINT = 9
    END = 10
    ERROR = 11

    def __str__(self):
        return str(self.lexeme) + " " + str(self.token_code)

    def __init__(self, lexeme, token_code):
        self.lexeme = lexeme
        self.token_code = token_code