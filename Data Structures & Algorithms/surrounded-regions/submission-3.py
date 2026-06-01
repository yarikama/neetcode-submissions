class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= R or c < 0 or c >= C or board[r][c] != 'O':
                return

            board[r][c] = 'P'

            for dr, dc in DIRS:
                dfs(r+dr, c+dc)


        for r in range(R):
            dfs(r, 0)
            dfs(r, C-1)

        for c in range(C):
            dfs(0, c)
            dfs(R-1, c)

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'P':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'