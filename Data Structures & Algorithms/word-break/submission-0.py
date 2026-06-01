class Solution:
    def wordBreak(
        self, 
        s: str, 
        wordDict: List[str]
    ) -> bool:
        if not wordDict:
            return False

        if not s:
            return True

        def dfs(i: int) -> bool:
            if i >= len(s):
                return True

            ans = False

            for word in wordDict:
                if len(word) > len(s) - i:
                    continue
                
                j = i
                all_same = True
                for c in range(len(word)):
                    if word[c] != s[j]:
                        all_same = False
                        break
                    j += 1

                if all_same:
                    ans = ans or dfs(j)

            return ans

        return dfs(0)
                         
                    
                    

        