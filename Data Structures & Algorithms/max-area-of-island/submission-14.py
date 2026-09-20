class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = float("-inf")
        n, m = len(grid), len(grid[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r: int, c: int) -> int:
            if min(r, c) < 0 or r > n - 1 or c > m - 1 or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            
            area = 1
            for dr, dc in dirs:
                area += dfs(r + dr, c + dc)
            return area

        for r in range(n):
            for c in range(m):
                res = max(res, dfs(r, c))

        return res
        