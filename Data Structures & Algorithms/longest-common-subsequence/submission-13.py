class Solution:
    def longestCommonSubsequence(
        self, 
        text1: str, 
        text2: str
    ) -> int:
        n, m = len(text1), len(text2)
        if n < m:
            text1, text2 = text2, text1
            n, m = m, n

        cache = [0] * (m + 1) # bottom up 

        for r in range(n-1, -1, -1):
            new_cache = [0] * (m + 1)
            for c in range(m-1, -1, -1):
                if text1[r] == text2[c]:
                    new_cache[c] = 1 + cache[c+1]
                else:
                    new_cache[c] = max(cache[c], new_cache[c+1])
            cache = new_cache

        return cache[0]
                    







    # def longestCommonSubsequence(
    #     self, 
    #     text1: str, 
    #     text2: str
    # ) -> int:
    #     R, C = len(text1) + 1, len(text2) + 1 # 內層補 0 -> 從 0 開始計算
    #     cache = [[0] * C for _ in range(R)]

    #     for i in range(R-1):
    #         for j in range(C-1):
    #             if text1[i] == text2[j]:
    #                 cache[i+1][j+1] = 1 + cache[i][j]
    #             else:
    #                 cache[i+1][j+1] = max(cache[i][j+1], cache[i+1][j])

    #     return cache[-1][-1]
        


    # def longestCommonSubsequence(
    #     self, 
    #     text1: str, 
    #     text2: str
    # ) -> int:
    #     cache = [[-1] * len(text2) for _ in range(len(text1))]

    #     def dfs(i: int, j: int) -> int:
    #         if i == len(text1) or j == len(text2):
    #             return 0

    #         if cache[i][j] != -1:
    #             return cache[i][j]

    #         if text1[i] == text2[j]:
    #             cache[i][j] = 1 + dfs(i+1, j+1)
    #         else:
    #             cache[i][j] = max(dfs(i+1, j), dfs(i, j+1))

    #         return cache[i][j]
            
    #     return dfs(0, 0)

    # def longestCommonSubsequence(
    #     self, 
    #     text1: str, 
    #     text2: str
    # ) -> int:
    #     def dfs(i: int, j: int) -> int:
    #         if i == len(text1) or j == len(text2):
    #             return 0

    #         if text1[i] == text2[j]:
    #             return 1 + dfs(i+1, j+1)

    #         return max(dfs(i+1, j), dfs(i, j+1))

    #     return dfs(0, 0)