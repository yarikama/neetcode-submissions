class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0, 0, 0)] # dist, r, c
        ROWS, COLS = len(heights), len(heights[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited = set()

        while heap:
            dist, r, c = heapq.heappop(heap)
            
            if (r, c) in visited:
                continue
            
            if (r, c) == (ROWS-1, COLS-1):
                return dist
            
            visited.add((r, c))

            for dr, dc in dirs:
                new_r, new_c = dr + r, dc + c

                if 0 <= new_r < ROWS and 0 <= new_c < COLS and (new_r, new_c) not in visited:
                    new_dist = abs(heights[new_r][new_c] - heights[r][c])
                    heapq.heappush(heap, (max(dist, new_dist), new_r, new_c))

