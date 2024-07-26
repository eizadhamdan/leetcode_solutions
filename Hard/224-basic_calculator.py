class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(tokens):
            stack = []
            num, sign = 0, 1
            res = 0
            for token in tokens:
                if token.isdigit():
                    num = num * 10 + int(token)
                elif token == '+':
                    res += sign * num
                    num, sign = 0, 1
                elif token == '-':
                    res += sign * num
                    num, sign = 0, -1
                elif token == '(':
                    stack.append(res)
                    stack.append(sign)
                    res, sign = 0, 1
                elif token == ')':
                    res += sign * num
                    num = 0
                    res *= stack.pop()  # This is the sign before the parenthesis
                    res += stack.pop()  # This is the result calculated before the parenthesis
            res += sign * num
            return res

        return evaluate([c for c in s if c != ' '])
    