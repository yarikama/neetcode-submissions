class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # cache = [1] * n
        # for r in range(m-2, -1, -1):
        #     for c in range(n-2, -1, -1):
        #         cache[c] += cache[c+1]

        # return cache[0]
        return math.comb(m-1 + n-1, m-1) 
        # The idea here is that the total number of down steps and right steps = m + n - 2, we only calculate the combination number it will have


        