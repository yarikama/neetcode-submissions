class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        prev, dp= [0] * n, [0] * n
        prev[-1] = 1
        for i in range(len(s)-1, -1, -1):
            dp[i] = 1
            for j in range(i+1, len(s)):
                if s[i] != s[j]:
                    dp[j] = max(dp[j-1], prev[j])
                else:
                    dp[j] = 2 + prev[j-1]
            prev = dp.copy()
        return dp[-1]
                