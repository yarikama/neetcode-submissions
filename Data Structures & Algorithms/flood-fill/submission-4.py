from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origin = image[sr][sc]
        if origin == color:
            return image

        n, m = len(image), len(image[0])

        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def dfs(r: int, c: int) -> None:
            if min(r, c) < 0 or r > n-1 or c > m-1 or image[r][c] != origin:
                return 

            image[r][c] = color

            for dr, dc in dirs:
                dfs(r+dr, c+dc)

        dfs(sr, sc)
        return image










        # origin = image[sr][sc]
        # if origin == color:
        #     return image

        # queue = deque([[sr, sc]])
        # dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # while queue:
        #     for i in range(len(queue)):
        #         r, c = queue.popleft()

        #         if min(r, c) < 0 or r > len(image)-1 or c > len(image[0])-1 or image[r][c] != origin:
        #             continue
                
        #         image[r][c] = color
                
        #         for dr, dc in dirs:
        #             queue.append([r+dr, c+dc])

        # return image