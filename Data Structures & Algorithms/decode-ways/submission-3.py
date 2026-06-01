class Solution:
    def numDecodings(self, s: str) -> int:
        cache = [ -1 if s[i] != '0' else 0 for i in range(len(s)) ]

        def dfs(i: int) -> int:
            if i > len(s) - 1: return 1

            if cache[i] != -1:
                return cache[i]

            value = 0
            j = i + 1
            if j < len(s) and int(s[i:j+1]) in range(1, 27):
                value += dfs(i+2)
            value += dfs(i+1)

            cache[i] = value
            return cache[i]

        return dfs(0)

            
        