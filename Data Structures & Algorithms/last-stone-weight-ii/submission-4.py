from collections import defaultdict

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Base Case
        cache = set()
        cache.add(sum(stones))
        
        for stone in stones:
            new_cache = set()
            for i in cache:
                new_cache.add(i)
                new_cache.add(i-2*stone)
            cache = new_cache


        cache = [abs(i) for i in cache]
        return min(cache)

    
        