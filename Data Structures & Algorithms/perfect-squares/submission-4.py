from math import ceil, sqrt, isqrt

class Solution:
    # def numSquares(self, n: int) -> int:
    #     dp = [float("inf")] * (n + 1)
    #     dp[0] = 0
    #     dp[1] = 1
        
    #     for i in range(1, n+1):
    #         for j in range(1, ceil(sqrt(i)) + 1):
    #             if i - j ** 2 < 0:
    #                 break
    #             dp[i] = min(dp[i], 1 + dp[i - j ** 2])

    #     return dp[-1]


    def numSquares(self, n: int) -> int:
        def is_square(x):
            r = isqrt(x)
            return r * r == x

        # 1 個
        if is_square(n):
            return 1

        # 4 個：n = 4^a(8b+7)
        m = n
        while m % 4 == 0:
            m //= 4
        if m % 8 == 7:
            return 4

        # 2 個
        for i in range(1, isqrt(n) + 1):
            if is_square(n - i * i):
                return 2

        # 其餘都是 3 個
        return 3