class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []

        col = set()
        pos_diag = set()
        neg_diag = set()
        board = [["."] * n for _ in range(n)]

        def dfs(r: int):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                
                dfs(r+1)

                board[r][c] = "."
                neg_diag.remove(r - c)
                pos_diag.remove(r + c)
                col.remove(c)

        dfs(0)
        return len(res)
            
        