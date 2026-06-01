from collections import deque

class Solution:

    def shortestPath(self, grid: List[List[int]]) -> int:
        # Constant
        ROWS, COLS = len(grid), len(grid[0])
        DEST = (ROWS-1, COLS-1)
        DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))

        # DSs 
        queue = deque()
        visited = set()  # backtracking
        
        # init
        length = 0
        start = (0, 0)
        queue.append(start)
        visited.add(start)

        # BFS
        while queue:
            # we are not using
            #   - for element in queue: 
            # is because we may do enque in BFS, need to ensure we are in one run
            for i in range(len(queue)):  

                # get current location
                r, c = queue.popleft()
                
                if (r, c) == DEST:
                    return length

                visited.add((r, c))

                for dr, dc in DIRS:
                    # Base Case
                    new_r, new_c = r+dr, c+dc
                    if (
                        new_r < 0 or new_c < 0 
                        or new_r == ROWS or new_c == COLS 
                        or (new_r, new_c) in visited 
                        or grid[new_r][new_c] == 1
                    ):
                        continue
                    queue.append((new_r, new_c))

            length += 1

        return -1



