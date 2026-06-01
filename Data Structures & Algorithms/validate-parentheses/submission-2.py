PREFIX = '({['
SUFFIX = ')}]'

class Solution:
    def is_stack_empty(self):
        return len(self.stack) == 0

    def check_letter(self, letter: str) -> bool:
        validation: bool = True
        
        if letter in PREFIX:
            self.stack.append(letter)
            return validation

        if self.is_stack_empty():
            return False

        if (letter == ')' and self.stack[-1] != '(') or \
        (letter == ']' and self.stack[-1] != '[') or \
        (letter == '}' and self.stack[-1] != '{'):
            return False
        else:
            self.stack.pop()

        return validation

    def isValid(self, s: str) -> bool:
        self.stack = []
        self.final_answer = True

        for letter in s:
            self.final_answer = self.check_letter(letter)
            if not self.final_answer:
                return self.final_answer

        if not self.is_stack_empty():
            return False

        return self.final_answer 





        