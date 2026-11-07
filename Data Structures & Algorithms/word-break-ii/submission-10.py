class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)

        def helper(L: int, R: int) -> List[str]:
            res = []

            if s[L:R] in wordDict:
                res.append(s[L:R])

            for i in range(L, R):
                if s[L:i] not in wordDict:
                    continue

                for suffix in helper(i, R):
                    res.append(s[L:i] + " " + suffix)

            return res

        return helper(0, len(s))