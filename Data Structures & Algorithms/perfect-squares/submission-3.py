from math import ceil, sqrt

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(1, n+1):
            for j in range(1, ceil(sqrt(i)) + 1):
                if i - j ** 2 < 0:
                    break
                dp[i] = min(dp[i], 1 + dp[i - j ** 2])

        return dp[-1]