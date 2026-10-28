class Solution:
    def knightDialer(self, n: int) -> int:
        if n <= 0:
            return 0

        steps = ((2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2))
        invalid_places = set([(3, 0), (3, 2)])

        grid = [[1] * 3 for _ in range(4)]
        grid[3][0] = 0
        grid[3][2] = 0

        for _ in range(n-1):
            new_grid = [[0] * 3 for _ in range(4)]

            for r in range(4):
                for c in range(3):
                    if (r, c) in invalid_places:
                        continue

                    for dr, dc in steps:
                        new_r, new_c = r + dr, c + dc

                        if 0 <= new_r < 4 and 0 <= new_c < 3 and (new_r, new_c) not in invalid_places:
                            new_grid[r][c] = (grid[new_r][new_c] + new_grid[r][c]) % 1000000007
            grid = new_grid

        return sum(sum(r) for r in grid) % 1000000007




        # def dfs(r: int, c: int, n: int) -> int:
        #     if n == 1:
        #         return 1

        #     if (r, c, n) in cache:
        #         return cache[(r, c, n)]

        #     total = 0
        #     for dr, dc in steps:
        #         new_r, new_c = r + dr, c + dc
        #         if 0 <= new_r < 4 and 0 <= new_c < 3 and (new_r, new_c) not in invalid_places:
        #             total += dfs(new_r, new_c, n-1)

        #     cache[(r, c, n)] = total
        #     return total

        # res = 0
        # for r in range(4):
        #     for c in range(3):
        #         if (r, c) not in invalid_places:
        #             res += dfs(r, c, n)

        return res