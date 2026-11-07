class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        
        dp = {}
        def helper(L: int, R: int) -> List[str]:
            res = set()

            if (L, R) in dp:
                return dp[(L, R)]

            if s[L:R] in wordDict:
                res.add(s[L:R])

            for i in range(L, R):
                res1 = helper(L, i)
                if not res1:
                    continue

                res2 = helper(i, R)
                if not res2:
                    continue

                for j in res1:
                    for k in res2:
                        res.add(j + " " + k)

            res = tuple(res)
            dp[(L, R)] = res
            return res

        return list(helper(0, len(s)))