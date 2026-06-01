from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0))
        q = deque()

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    q.append((i, j))

        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                value = grid[x][y]
                for dx, dy in DIRS:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < R and 0 <= new_y < C and grid[new_x][new_y] > value + 1:
                        grid[new_x][new_y] = value + 1
                        q.append((new_x, new_y))









        