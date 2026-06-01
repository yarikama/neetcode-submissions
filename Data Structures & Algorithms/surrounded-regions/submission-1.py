class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(r: int, c: int) -> bool:
            if r < 0 or r >= R or c < 0 or c >= C or board[r][c] == 'Q':
                return False

            if board[r][c] == 'X' or board[r][c] == 'P':
                return True

            board[r][c] = 'P'

            ans = True
            for dr, dc in DIRS:
                ans = ans and dfs(r+dr, c+dc)

            if ans:
                board[r][c] = 'X'
            else:
                board[r][c] = 'Q'

            return ans

        for r in range(R):
            for c in range(C):
                dfs(r, c)

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'Q':
                    board[r][c] = 'O'



        