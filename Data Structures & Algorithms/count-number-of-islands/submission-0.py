class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(
            grid: List[List[int]], r: int, c: int 
        ) -> None:
            if (
                r == -1 or c == -1 
                or r == ROWS or c == COLS
                or grid[r][c] == '0'
            ):
                return

            grid[r][c] = '0'
            
            dfs(grid, r-1, c)
            dfs(grid, r+1, c)
            dfs(grid, r, c-1)
            dfs(grid, r, c+1)

            return

        a = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] =='1':
                    dfs(grid, i, j)
                    a += 1

        return a



