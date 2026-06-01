class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text1), len(text2)
        grid = [[0] * COLS] * ROWS

        for row in range(ROWS-1, -1, -1):
            for col in range(COLS-1, -1, -1):
                if text1[row] == text2[col]:
                    add_up = grid[row + 1][col + 1] if ROWS > row + 1 and COLS > col + 1 else 0
                    grid[row][col] = 1 + add_up
                else:
                    right = grid[row][col+1] if COLS > col+1 else 0
                    left = grid[row+1][col] if ROWS > row+1 else 0
                    grid[row][col] = max(right, left)

        return grid[0][0]


        