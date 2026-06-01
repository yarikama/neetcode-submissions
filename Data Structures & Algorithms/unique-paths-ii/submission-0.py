class Solution:
    def uniquePathsWithObstacles(
        self, 
        obstacleGrid: List[List[int]]
    ) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        for col in range(COLS-1, -1, -1):
            if obstacleGrid[ROWS-1][col] == 1:
                for i in range(col):
                     obstacleGrid[ROWS-1][i] = 1

        for row in range(ROWS-1, -1, -1):
            if obstacleGrid[row][COLS-1] == 1:
                for i in range(row):
                     obstacleGrid[i][COLS-1] = 1
            
        for row in range(ROWS):
            for col in range(COLS):
                if obstacleGrid[row][col] == 0:
                    obstacleGrid[row][col] = 1
                else:
                    obstacleGrid[row][col] = 0

        for row in range(ROWS-2, -1, -1):
            for col in range(COLS-2, -1, -1):
                obstacleGrid[row][col] = obstacleGrid[row+1][col] + obstacleGrid[row][col+1]

        return obstacleGrid[0][0]
