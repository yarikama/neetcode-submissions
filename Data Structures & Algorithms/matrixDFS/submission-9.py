class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DES = (ROWS - 1, COLS - 1)
        visited = set()

        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r == ROWS or c == ROWS or (r, c) in visited or grid[r][c] == 1:
                return 0

            if (r, c) == DES:
                return 1

            visited.add((r, c))

            result = (
                dfs(r + 1, c) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r, c - 1) 
            )

            visited.remove((r, c)) # backtracking

            return result

        return dfs(0, 0)