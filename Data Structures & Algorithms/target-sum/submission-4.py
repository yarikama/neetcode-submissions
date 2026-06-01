from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0
            
        cache = defaultdict(int)
        cache[0] = 1

        for num in nums:
            new_cache = defaultdict(int) # 因為可能會污染，所以要用新的
            for cap, num_path in cache.items():
                new_cache[cap+num] += num_path
                new_cache[cap-num] += num_path
            cache = new_cache

        return cache[target]
        