class Solution:
    def checkValidString(self, s: str) -> bool:
        star, left, right = 0, 0, 0 
        for char in s:
            if char == '(':
                left += 1
            if char == ')':
                right += 1
            if char == '*':
                star += 1

        if abs(left - right) < star:
            return True
        return False
                
                
        