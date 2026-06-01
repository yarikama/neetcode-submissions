from heapq import heappush, heappop

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
        pq = [(grid[0][0], (0, 0))] # weight, location
        shortest_path = {}
        while pq:
            w1, loc = heappop(pq)
            if loc == (ROWS-1, COLS-1):
                return w1
            if loc in shortest_path:
                continue
            shortest_path[loc] = w1

            for dx, dy in DIRS:
                nx, ny = dx + loc[0], dy + loc[1]
                if nx < 0 or ny < 0 or nx >= ROWS or ny >= COLS or (nx, ny) in shortest_path:
                    continue
                heappush(pq, (max(w1, grid[nx][ny]), (nx, ny))) # cool

        return shortest_path[ROWS-1][COLS-1]



             

