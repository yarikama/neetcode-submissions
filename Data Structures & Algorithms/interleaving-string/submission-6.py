class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        
        cache = [[None] * (len(s2)+1) for _ in range(len(s1)+1)]
        cache[len(s1)][len(s2)] = True

        def dfs(i: int, j: int) -> bool:
            if cache[i][j] is not None:
                return cache[i][j]

            if i < len(s1) and s1[i] == s3[i+j]:
                if dfs(i+1, j):
                    cache[i][j] = True
                    return cache[i][j]
            if j < len(s2) and s2[j] == s3[i+j]:
                if dfs(i, j+1):
                    cache[i][j] = True
                    return cache[i][j]
            
            cache[i][j] = False
            return cache[i][j]

        return dfs(0, 0)