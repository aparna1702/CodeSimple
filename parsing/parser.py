import sys
from CodeSimple import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.token_index = 0
        self.advance()

    def advance(self):
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
        else:
            self.current_token = None

    def parse(self):
        return self.expr()

    def factor(self):
        token = self.current_token

        if token.type in (TT_INT, TT_FLOAT):
            self.advance()
            return token

        elif token.type == TT_LPAREN:
            self.advance()
            result = self.expr()
            if self.current_token.type == TT_RPAREN:
                self.advance()
                return result

        return None

    def term(self):
        return self.bin_op(self.factor, (TT_MUL, TT_DIV, TT_MOD))

    def expr(self):
        return self.bin_op(self.term, (TT_PLUS, TT_MINUS))

    def bin_op(self, func, ops):
        left = func()

        while self.current_token and self.current_token.type in ops:
            op = self.current_token
            self.advance()
            right = func()

            left = Token(op.type, value=(left, op, right))

        return left

# Example usage
text = input('CodeSimple > ')
tokens, error = run(text)

if error:
    print(error.as_string())
else:
    parser = Parser(tokens)
    result = parser.parse()
    print(result)
