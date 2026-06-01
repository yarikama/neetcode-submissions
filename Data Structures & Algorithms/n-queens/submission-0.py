class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def dfs(
            row_idx: int, 
            unused_col: Set[int], 
            unused_sum: Set[int],
            unused_diff: Set[int],
            curr_map: List[List[str]],
        ) -> None:
            nonlocal n

            if n == row_idx:
                res.append([ "".join(r) for r in curr_map ])

            for c in range(n):
                if c not in unused_col or row_idx+c not in unused_sum or row_idx-c not in unused_diff or curr_map[row_idx][c] == 'Q':
                    continue

                unused_col.remove(c)
                unused_sum.remove(row_idx+c)
                unused_diff.remove(row_idx-c)
                curr_map[row_idx][c] = 'Q'
                dfs(
                    row_idx+1, 
                    unused_col, 
                    unused_sum,
                    unused_diff,
                    curr_map
                )
                curr_map[row_idx][c] = '.'
                unused_diff.add(row_idx-c)
                unused_sum.add(row_idx+c)
                unused_col.add(c)


        map = [["."] * n for _ in range(n)]
        dfs(0, set(range(n)), set(range(2*n-1)), set(range(-(n-1), n)), map)
        return res
            
        