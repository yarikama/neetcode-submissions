class Solution:
    def uniquePathsWithObstacles(
        self, 
        obstacleGrid: List[List[int]]
    ) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[ROWS-1][COLS-1] != 0:
            return 0

        for row in range(ROWS):
            for col in range(COLS):
                if obstacleGrid[row][col] == 0:
                    obstacleGrid[row][col] = 1
                else:
                    obstacleGrid[row][col] = 0

        for row in range(ROWS-1, -1, -1):
            for col in range(COLS-1, -1, -1):
                if row == ROWS-1 and col == COLS-1:
                    continue
                elif obstacleGrid[row][col] == 0:
                    continue
                elif row == ROWS-1:
                    obstacleGrid[row][col] = obstacleGrid[row][col+1]
                elif col == COLS-1:
                    obstacleGrid[row][col] = obstacleGrid[row+1][col]
                else:
                    obstacleGrid[row][col] = obstacleGrid[row+1][col] + obstacleGrid[row][col+1]

        return obstacleGrid[0][0]
