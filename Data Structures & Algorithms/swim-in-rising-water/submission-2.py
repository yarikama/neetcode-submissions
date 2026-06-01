from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS, DIRS = len(grid), len(grid[0]), ((0, 1), (1, 0), (0, -1), (-1, 0))
        DEST = (ROWS-1, COLS-1)

        # weight, xi, yi
        pq = [(grid[0][0], 0, 0)]
        sp = {}

        while pq:
            wi, xi, yi = heappop(pq)
            if (xi, yi) in sp:
                continue
            if (xi, yi) == DEST:
                return wi
            sp[(xi, yi)] = wi

            for dx, dy in DIRS:
                xj, yj = xi+dx, yi+dy
                if (
                    xj < 0 or yj < 0 
                    or xj >= ROWS or yj >= COLS 
                    or (xj, yj) in sp
                ):
                    continue
                heappush(pq, (max(wi, grid[xj][yj]), xj, yj))
             

