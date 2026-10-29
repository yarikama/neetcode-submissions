class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1

        if n == 3:
            return 2

        dp = {1: 1, 2: 2}

        def helper(n: int) -> int:
            if n in dp:
                return dp[n]

            maximum = n
            for i in range(2, n // 2 + 1):
                maximum = max(maximum, i * helper(n - i))

            dp[n] = maximum
            return maximum

        res = helper(n)
        return res

            
