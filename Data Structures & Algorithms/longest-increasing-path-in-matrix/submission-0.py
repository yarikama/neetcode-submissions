class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        res = [[0] * m for _ in range(n)]
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(r: int, c: int) -> int: 
            if res[r][c] != 0:
                return res[r][c]

            max_path = 0
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < n and 0 <= nc < m and matrix[r][c] < matrix[nr][nc]:
                    max_path = max(max_path, dfs(nr, nc))
            res[r][c] = 1 + max_path
            return res[r][c] 

        longest = 0
        for r in range(n):
            for c in range(m):
                longest = max(longest, dfs(r, c))

        return longest



        