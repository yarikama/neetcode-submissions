PREFIX = '({['
SUFFIX = ')}]'

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        self.final_answer = True

        for letter in s:
            self.check_letter(letter, stack)

        if len(stack) != 0:
            return False

        return self.final_answer 

    def check_letter(self, letter: str, stack: list):
        if letter in PREFIX:
            stack.append(letter)
        else:
            if letter == ')' and stack[-1] != '(':
                self.final_answer = False
            elif letter == ']' and stack[-1] != '[':
                self.final_answer = False
            elif letter == '}' and stack[-1] != '{':
                self.final_answer = False
            else:
                stack.pop()



        