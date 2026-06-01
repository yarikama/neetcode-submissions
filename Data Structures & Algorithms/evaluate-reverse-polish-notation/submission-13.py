class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.split('-')[-1].isdigit():
                stack.append(int(token))
            else:
                print(stack, token)            
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                if token == '-':
                    stack.append(num1 - num2)
                if token == '*':
                    stack.append(num1 * num2)
                if token == '/':
                    if num2 != 0:
                        stack.append(int(num1 / num2))
                    else:
                        stack.append(0)

        
        
        return stack.pop()

