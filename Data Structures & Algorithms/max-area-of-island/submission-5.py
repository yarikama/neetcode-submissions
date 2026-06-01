class Solution:
    def maxAreaOfIsland(
        self, 
        grid: List[List[int]]
    ) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            # if (
            #     r == ROWS or c == COLS 
            #     or r == -1 or c == -1
            #     or grid[i][j] == 0
            # ):
            #     return 0

            grid[i][j] = 0
            count = 1
            count += (dfs(r + 1, c))
            count += (dfs(r - 1, c))
            count += (dfs(r, c + 1))
            count += (dfs(r, c - 1))
            return count

        max_area = 0
        for i in range(ROWS):
            for j in range(COLS):
                area = dfs(i, j)
                max_area = max(max_area, area)

        return max_area