class Solution:
    def checkValidString(self, s: str) -> bool:
        star, num = 0, 0 
        for char in s:
            if char == '(':
                num += 1
            if char == ')':
                num -= 1
            if char == '*':
                star += 1
            
            if num + star < 0:
                return False 

        if abs(num) > star:
            return False
        return True
                
                
# )((*)