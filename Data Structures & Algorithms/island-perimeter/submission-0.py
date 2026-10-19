class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total = 0
        for r in range(rows):
            for c in range(cols):
                curr = 0
                if grid[r][c] == 1:
                    curr += 4
                    if r-1 >= 0 and grid[r-1][c] == 1:
                        curr -= 2
                    if c-1 >= 0 and grid[r][c-1] == 1:
                        curr -= 2
                total += curr

        return total


                
            
                

        