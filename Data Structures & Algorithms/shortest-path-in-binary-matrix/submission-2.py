from collections import deque
from itertools import product

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = tuple(x for x in product((1, 0, -1), repeat=2) if any(x))

        l = 0
        q = deque([[0, 0]])
        while q:
            l += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                
                if min(r, c) < 0 or r > n - 1 or c > m - 1 or grid[r][c] == 1:
                    continue

                if (r, c) == (n - 1, m - 1):
                    return l

                grid[r][c] = 1

                for dr, dc in dirs:
                    q.append((r + dr, c + dc))


        return -1


                