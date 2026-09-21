class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1

        n, m = len(word1), len(word2)

        if m == 0:
            return n

        cache = list(range(m+2))
        
        for r in range(1, n+1):
            new_cache = [0] * (m + 1)
            new_cache[0] = r
            for c in range(1, m+1):
                if word1[r-1] == word2[c-1]:
                    new_cache[c] = cache[c-1]
                else:
                    new_cache[c] = 1 + min(new_cache[c-1], cache[c-1], cache[c])
            cache = new_cache

        return cache[-1]
                    
        