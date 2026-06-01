from collections import deque

class Solution:
    def shortestPath(
        self, 
        grid: List[List[int]]
    ) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DESTINATION = (ROWS - 1, COLS - 1)
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visit = set()
        queue = deque()
        queue.append((0,0))
        length = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if (r, c) == DESTINATION:
                    return length

                for diff_r, diff_c in moves:
                    new_r, new_c = r + diff_r, c + diff_c 
                    if (
                        min(new_r, new_c) < 0
                        or new_r == ROWS or new_c == COLS
                        or (new_r, new_c) in visit
                        or grid[new_r][new_c] == 1  
                    ):
                        continue

                    queue.append((new_r, new_c))
                    visit.add((new_r, new_c))

            length += 1

        return -1

        