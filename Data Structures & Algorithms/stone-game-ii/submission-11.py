class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        dp = {}

        # def dfs(L: int, M: int, isA: bool) -> Tuple[int]:
        #     if L >= n:
        #         return 0, 0

        #     if (L, M, isA) in dp:
        #         return dp[(L, M, isA)]

        #     curr = A = B = 0
        #     for i in range(L, min(n, L + 2 * M)):
        #         curr += piles[i]

        #         new_A, new_B = dfs(i+1, max(i-L+1, M), not isA)

        #         if isA:
        #             if curr + new_A > A:
        #                 A, B = curr + new_A, new_B

        #         else:
        #             if curr + new_B > B:
        #                 A, B = new_A, curr + new_B

        #     dp[(L, M, isA)] = A, B
        #     return A, B

        # return dfs(0, 1, True)[0]


        def dfs(L: int, M: int, is_Alice: bool) -> int:
            if L >= n:
                return 0
            key = (L, M, is_Alice)
            if key in dp:
                return dp[key]

            res = 0 if is_Alice else float("inf")
            curr = 0
            for i in range(L, min(n, L + 2 * M)):
                curr += piles[i]
                nxt = dfs(i + 1, max(M, i - L + 1), not is_Alice)
                if is_Alice:
                    res = max(res, curr + nxt)
                else:
                    res = min(res, nxt)

            dp[key] = res
            return res

        return dfs(0, 1, True)