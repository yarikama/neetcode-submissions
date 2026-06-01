class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < len(s):
            while l < len(s) - 1 and not('A' <= s[l] and s[l] <= 'z'):
                l += 1
            while r > 1 and not('A' <= s[r] and s[r] <= 'z'):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True



        