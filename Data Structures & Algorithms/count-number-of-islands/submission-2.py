class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        def dfs(r: int, c: int) -> None:
            if min(r, c) < 0 or r > n - 1 or c > m - 1 or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            for dr, dc in dirs:
                dfs(r+dr, c+dc)

        res = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == "1":
                    res += 1
                    dfs(r, c)

        return res