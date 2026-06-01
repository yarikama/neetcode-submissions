class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print(stack)            
            if token.split('-')[-1].isdigit():
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                print(num2, num1)
                if token == '+':
                    stack.append(num1 + num2)
                if token == '-':
                    stack.append(num1 - num2)
                if token == '*':
                    stack.append(num1 * num2)
                if token == '/':
                    if num1 != 0:
                        print(num1, num2, num1//num2)
                        stack.append(num2 // num1)
                    else:
                        stack.append(0)
        print(stack)            
        
        
        return stack.pop()

