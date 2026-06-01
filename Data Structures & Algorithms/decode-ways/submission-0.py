class Solution:
    def numDecodings(self, s: str) -> int:
        

        def dfs(i: int) -> int:
            if i >= len(s) - 1: return 1

            if s[i] == '0':
                return 0

            value = 0
            j = i + 1
            if j < len(s) and int(s[i:j+1]) in range(1, 27):
                value += dfs(i+2)
            value += dfs(i+1)

            return value

        return dfs(0)

            
        