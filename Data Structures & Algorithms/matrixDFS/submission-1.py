class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DESTINATION = (ROWS - 1, COLS - 1)

        def dfs(grid, r, c, visit) -> int:
            if (r, c) == DESTINATION:
                return 1
            if (r == -1 or c == -1 
                or r == ROW or C == ROW
                or visit[(r, c)] == 1
                or grid[r][c] == 1
            ):
                return 0

            visit.add((r, c))

            count = 0
            count += dfs(grid, r+1, c, visit)
            count += dfs(grid, r-1, c, visit)
            count += dfs(grid, r, c+1, visit)
            count += dfs(grid, r, c-1, visit)

            visit.remove((r, c))
            return count
        

        return dfs(grid, 0, 0, set())