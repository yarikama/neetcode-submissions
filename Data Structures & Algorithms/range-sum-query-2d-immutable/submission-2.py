class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        
        self.ROWS, self.COLS = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * self.COLS for _ in range(self.ROWS)]

        for row in range(self.ROWS):
            for col in range(self.COLS):
                left_upper = self.prefix_sum[row - 1][col - 1] if row > 0 and col > 0 else 0
                left = self.prefix_sum[row - 1][col] if row > 0 else 0
                upper = self.prefix_sum[row][col - 1] if col > 0 else 0
                self.prefix_sum[row][col] = left + upper - left_upper + matrix[row][col]
        
        for row in matrix:
            print(row)

        print('x' * 10)

        for row in self.prefix_sum:
            print(row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix_sum[row2][col2] 
        left_upper = self.prefix_sum[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        upper = self.prefix_sum[row2][col1 - 1] if col1 > 0 else 0
        left = self.prefix_sum[row1 - 1][col2] if row1 > 0 else 0

        return total + left_upper - upper - left



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
