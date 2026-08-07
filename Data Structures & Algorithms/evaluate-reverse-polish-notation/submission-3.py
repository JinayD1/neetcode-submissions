class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = ['+', '*', '-', '/']
        for token in tokens:
            if token in symbols:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(self.calculate(token, int(num1), int(num2)))
            else:
                stack.append(token)
        return int(stack.pop())
    
    def calculate(self, symbol, number1, number2):
        if symbol == '+':
            return number1 + number2
        elif symbol == '*':
            return number1 * number2
        elif symbol == '-':
            return number2 - number1
        else:
            return number2 / number1