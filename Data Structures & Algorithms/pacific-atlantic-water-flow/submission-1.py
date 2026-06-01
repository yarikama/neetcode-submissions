class Solution:
    def pacificAtlantic(
        self, 
        heights: List[List[int]]
    ) -> List[List[int]]:
        R, C = len(heights), len(heights[0]) #1, 1
        cache = {}
        visited = set()
        DIRS = ((0, 1), (-1, 0), (0, -1), (1, 0))

        def dfs(r: int, c: int, prev_val: int) -> Tuple[bool, bool]:
            if (r == 2 and c == 1): print("HERE")
            if (r, c) in cache: 
                if (r == 2 and c == 1): print("Cached")
                return cache[(r, c)]

            pac, atl = False, False

            if r < 0 or c < 0:
                pac = True

            if r >= R or c >= C:
                atl = True

            if pac or atl:
                cache[(r, c)] = (pac, atl)
                if (r == 2 and c == 1): print("Outted")
                return pac, atl

            if prev_val < heights[r][c]:
                return False, False

            visited.add((r, c))

            for dr, dc in DIRS:
                new_r, new_c = r+dr, c+dc
                if (new_r, new_c) not in visited:
                    new_pac, new_atl = dfs(new_r, new_c, heights[r][c])
                    pac, atl = new_pac or pac, new_atl or atl
            
            visited.remove((r, c))
            cache[(r, c)] = (pac, atl)
            return pac, atl

        for r in range(R):
            for c in range(C):
                dfs(r, c, heights[r][c])

        ans = []
        for key, (pac, atl) in cache.items():
            if pac and atl:
                ans.append(key)

        return ans

            
            



                







                


            

            

        