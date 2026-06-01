class Solution:
    def isValid(self, s: str) -> bool:
        self.stack = []
        self.final_answer = True

        for letter in s:
            self.check_letter(letter)

        if len(self.stack) != 0:
            return False

        return self.final_answer 

    def check_letter(self, letter: str):
        if letter in '({[':
            self.stack.append(letter)

        if (letter == ')' and self.stack[-1] != '(') or \
        (letter == ']' and self.stack[-1] != '[') or \
        (letter == '}' and self.stack[-1] != '{'):
            self.final_answer = False
            self.stack.pop()



        