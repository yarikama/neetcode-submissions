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
            visited.add((r, c))

            if (r, c) == (ROWS - 1, COLS - 1):
                return dist

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    diff = abs(heights[nr][nc] - heights[r][c])
                    heapq.heappush(heap, (max(dist, diff), nr, nc))