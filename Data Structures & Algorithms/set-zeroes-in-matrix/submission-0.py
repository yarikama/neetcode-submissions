class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])
        skip_rows, skip_cols = set(), set()
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    skip_rows.add(r)
                    skip_cols.add(c)
        
        for r in skip_rows:
            for c in range(C):
                matrix[r][c] = 0 

        for r in range(R):
            for c in skip_cols:
                matrix[r][c] = 0 
                    
        
        