class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0

        col = set()
        pos_diag = set()
        neg_diag = set()

        def dfs(r: int):
            nonlocal res
            
            if r == n:
                res += 1
                return

            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                
                dfs(r+1)

                neg_diag.remove(r - c)
                pos_diag.remove(r + c)
                col.remove(c)

        dfs(0)
        return res
        