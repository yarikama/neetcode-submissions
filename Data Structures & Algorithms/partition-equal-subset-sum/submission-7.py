class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Check whether this can be divide by 2
        if (sum_nums := sum(nums)) % 2 == 1:
            return False
        target = sum_nums // 2

        cache = [False] * (target+1)
        cache[0] = True

        for item in nums:
            for cap in range(target, item-1, -1):
                cache[cap] = cache[cap] or cache[cap - item]
                if cache[target]: return True

        return False

