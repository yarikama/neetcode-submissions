# 1 2 3       1 4 7
# 4 5 6   ->  2 5 8
# 7 8 9       3 6 9


# 1 2  1 3  3 1 
# 3 4  2 4  4 2

# 2 1
# 4 3
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])
        for r in range(R):
            for c in range(r, C):
                if r == c: continue
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for row in matrix:
            row.reverse()