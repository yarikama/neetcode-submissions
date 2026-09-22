class Solution:
    def numDistinct(self, s: str, t: str) -> int:        
        n, m = len(s), len(t)

        if m > n:
            return 0

        cache = [1] + [0] * m

        for r in range(1, n+1):
            for c in range(m, 0, -1):
                if s[r-1] == t[c-1]:
                    cache[c] += cache[c-1]
        
        return cache[-1] 


