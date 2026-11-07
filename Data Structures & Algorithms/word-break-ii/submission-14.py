class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # wordDict = set(wordDict)
        # dp = {}

        # def helper(L: int, R: int) -> List[str]:
        #     res = []

        #     if (L, R) in dp:
        #         return dp[(L, R)]

        #     if s[L:R] in wordDict:
        #         res.append(s[L:R])

        #     for i in range(L, R):
        #         if s[L:i] not in wordDict:
        #             continue

        #         for suffix in helper(i, R):
        #             res.append(s[L:i] + " " + suffix)

        #     dp[(L, R)] = res
        #     return res

        # return helper(0, len(s))


        ########################################
        # wordDict = set(wordDict)
        # dp = {}
        # R = len(s)

        # def helper(L: int) -> List[str]:
        #     res = []

        #     nonlocal R

        #     if (L, R) in dp:
        #         return dp[(L, R)]

        #     if s[L:R] in wordDict:
        #         res.append(s[L:R])

        #     for i in range(L, R):
        #         if s[L:i] not in wordDict:
        #             continue

        #         for suffix in helper(i):
        #             res.append(s[L:i] + " " + suffix)

        #     dp[(L, R)] = res
        #     return res

        # return helper(0)
        ###########################################
        wordDict = set(wordDict)
        n = len(s)
        dp = [[] for _ in range(n+1)]
        dp[0].append("")

        for R in range(1, n+1):
            for L in range(R):
                if s[L:R] in wordDict:
                    for prefix in dp[L]:
                        dp[R].append((prefix + " " + s[L:R]).strip())
                        
        return dp[n]
