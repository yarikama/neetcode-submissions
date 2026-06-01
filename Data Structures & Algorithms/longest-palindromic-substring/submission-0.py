class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = 0
        maxL, maxR = 0, 0

        for i in range(len(s)):
            L, R = i, i
            while L >= 0 and R < len(s):
                if s[L] != s[R]:
                    break

                if R - L + 1 > length:
                    maxL, maxR = L, R
                    length = R - L + 1
                L -= 1
                R += 1

            L, R = i, i+1
            while L >= 0 and R < len(s):
                if s[L] != s[R]:
                    break

                if R - L + 1 > length:
                    maxL, maxR = L, R
                    length = R - L + 1      

                L -= 1
                R += 1

        return s[maxL:maxR+1]
        