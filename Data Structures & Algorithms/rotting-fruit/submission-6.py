from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        q = deque( (r, c) for r in range(n) for c in range(m) if grid[r][c] == 2)

        s = sum(grid[r][c] for r in range(n) for c in range(m))

        if not q and s == 0:
            return 0
        
        if not q and s > 0:
            return -1

        l = 0

        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        while q:
            
            is_banana = False

            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    new_r, new_c = r + dr, c + dc
                    
                    if min(new_r, new_c) < 0 or new_r > n - 1 or new_c > m - 1 or grid[new_r][new_c] != 1: 
                        continue
                    
                    grid[new_r][new_c] = 2
                    q.append((new_r, new_c))
                    is_banana = True


            if is_banana:
                l += 1

        return l if not any(grid[r][c] == 1 for r in range(n) for c in range(m)) else -1