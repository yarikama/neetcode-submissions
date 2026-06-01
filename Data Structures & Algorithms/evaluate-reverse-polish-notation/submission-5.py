class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [0, 0]
        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                if token == '-':
                    stack.append(num1 - num2)
                if token == '*':
                    stack.append(num1 * num2)
                if token == '/':
                    stack.append(num1 // num2)
        return stack.pop()

