###############
# CONSTANTS
################
DIGITS = '0123456789'
KEYWORDS = ['namaste', 'dhanywaad', 'dekhao', 'jab tk', 'kram', 'agar', 'ya ye', 'ni tu', 'dashamlav', 'akshar',
            'karya', 'btao', 'suno', 'bus', 'chlte rho', 'tb tk', 'badlo', 'mamla', 'theek h', 'sahi ya galat',
            'sahi', 'galat', 'barabar h', 'barabar_nhi_h', 'chota h', 'bada h', 'ya', 'ye bhi', 'jodo', 'ghatao',
            'guna', 'bhag', 'shesh', 'chota ya barabar', 'bada ya barabar']

##############################
# ERRORS
##########
class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        return result

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__('Illegal Character', details)

# TOKENS
####################
TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MULTIPLY'
TT_DIV = 'DIVISION'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_KEYWORD = 'KEYWORD'
TT_MOD='Modulous'
TT_PRINT='Print'
TT_WHILE='jabtk'
TT_FOR='kram'


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'

###############
# LEXER
#################

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def make_tokens(self):
        tokens = []

        while self.current_char is not None:
            if self.current_char in '\t ':
                self.advance()
            elif self.current_char=='#':
                while self.current_char != '\n':
                    self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char.isalpha():
                tokens.append(self.make_keyword())
            else:
                char = self.current_char
                self.advance()
                return [], IllegalCharError("'" + char + "'")

        return tokens, None

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char is not None and (self.current_char in DIGITS + '.'):
            if self.current_char == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))

    def make_keyword(self):
        word = ''
        while self.current_char is not None and (self.current_char.isalpha() or self.current_char.isspace()):
            word += self.current_char
            self.advance()

        if word.strip() in KEYWORDS:
            if word.strip()=="jodo":
             return Token(TT_PLUS,word.strip())
            elif word.strip()=="ghatao":
                return Token(TT_MINUS,word.strip())
            elif word.strip()=="guna":
                return Token(TT_MUL, word.strip())
            elif word.strip()=="bhag":
                return Token(TT_DIV, word.strip())
            elif word.strip()=="shesh":
                return Token(TT_MOD, word.strip())
            elif word.strip()=="dekhao":
                return Token(TT_PRINT, word.strip())
            else:
             return Token(TT_KEYWORD, word.strip())

#######################
# RUN
#############
def run(text):
    lexer = Lexer(text)
    tokens, error = lexer.make_tokens()

    return tokens, error
