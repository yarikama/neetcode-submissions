class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) < 2:
            return 1 if s[0] != '0' else 0

        if s[-2] == '0': return 0

        cache = [ -1 if s[i] != '0' else 0 for i in range(len(s)) ]
        cache[-1] = 1
        cache[-2] = 2 if int(s[-2:]) in range(11, 27) else 1

        for i in range(len(s)-3, -1, -1):
            if s[i] == '0':
                continue

            cache[i] = 0
            if int(s[i:i+2]) in range(10, 27):
                cache[i] += cache[i+2]
            cache[i] += cache[i+1]

        return cache[0]

        # def dfs(i: int) -> int:
        #     if i > len(s) - 1: return 1

        #     if cache[i] != -1:
        #         return cache[i]

        #     value = 0
        #     j = i + 1
        #     if j < len(s) and int(s[i:j+1]) in range(1, 27):
        #         value += dfs(i+2)
        #     value += dfs(i+1)

        #     cache[i] = value
        #     return cache[i]

        # return dfs(0)

            
        