class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0

        n, m = len(obstacleGrid), len(obstacleGrid[0])
        cache = [0] * m
        for c in range(m-1, -1, -1):
            if obstacleGrid[-1][c] == 0:
                cache[c] = 1
            else:
                break

        for r in range(n-2, -1, -1):
            for c in range(m-1, -1, -1):
                if obstacleGrid[r][c] == 1:
                    cache[c] = 0
                elif c != m-1:
                    cache[c] += cache[c+1]
        
        return cache[0]
