class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_s = ""
        for letter in s:
            if 'A' <= letter <= 'Z' or 'a' <= letter <= 'z':
                new_s += letter

        print(new_s)

        l, r = 0, len(new_s)-1
        
        while l < len(new_s):
            if new_s[l].lower() != new_s[r].lower():
                return False
            l += 1
            r -= 1

        return True



        