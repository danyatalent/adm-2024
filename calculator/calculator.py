from number import *

class Calculator:
    def __init__(self, lhs: Number, rhs: Number, operation: str, notation: int) -> None:
        self.lhs = lhs
        self.rhs = rhs
        self.operation = operation
        self.notation = notation
    def calculate(self) -> Number:
        if self.operation == "+":
            res = add(self.lhs, self.rhs, self.notation)
            res.convert_from_10(self.notation)
            return res
        elif self.operation == '-':
            res = sub(self.lhs, self.rhs, self.notation)
            res.convert_from_10(self.notation)
            return res
        elif self.operation == '*':
            res = multiply(self.lhs, self.rhs, self.notation)
            res.convert_from_10(self.notation)
            return res
        elif self.operation == '/':
            res = division(self.lhs, self.rhs, self.notation)
            res.convert_from_10(self.notation)
            return res