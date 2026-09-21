class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [1] * n
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                cache[c] += cache[c+1]

        return cache[0]



        