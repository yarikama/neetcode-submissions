class Solution:
    def climbStairs(
        self, 
        n: int
    ) -> int:
        # # Base Case
        if n == 1:
            return 1

        if n == 2:
            return 2

        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        cache = [1, 2]
        i = 2
        while i < n:
            tmp = cache[1]
            cache[1] += cache[0]
            cache[0] = tmp
            i+=1
        return cache[-1]
