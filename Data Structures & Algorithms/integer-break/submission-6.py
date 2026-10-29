class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1

        if n == 3:
            return 2

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = i
            for j in range(2, i // 2 + 1):
                dp[i] = max(dp[i], j * dp[i-j])

        return dp[-1]

        # def helper(n: int) -> int:
        #     if n in dp:
        #         return dp[n]

        #     maximum = n
        #     for i in range(2, n // 2 + 1):
        #         maximum = max(maximum, i * helper(n - i))

        #     dp[n] = maximum
        #     return maximum

        # res = helper(n)
        # return res

            
