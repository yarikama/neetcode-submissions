class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(L: int, R: int, isRemoved: bool = False) -> bool:
            while L < R:
                if s[L] == s[R]:
                    L += 1
                    R -= 1
                elif isRemoved:
                    return False
                else:
                    return helper(L+1, R, True) or helper(L, R-1, True) 

            return True

        return helper(0, len(s)-1)

        
        