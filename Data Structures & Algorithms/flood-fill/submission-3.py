from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origin = image[sr][sc]
        if origin == color:
            return image

        queue = deque([[sr, sc]])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                if min(r, c) < 0 or r > len(image)-1 or c > len(image[0])-1 or image[r][c] != origin:
                    continue
                
                image[r][c] = color
                
                for dr, dc in dirs:
                    queue.append([r+dr, c+dc])

        return image