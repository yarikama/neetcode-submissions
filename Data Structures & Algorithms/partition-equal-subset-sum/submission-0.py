class Solution:
    # MIMK
    def canPartition(self, nums: List[int]) -> bool:
        # Check whether this can be divide by 2
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        target = sum_nums // 2

        # 181
        cache = [0] * (target + 1)
        for item in range(len(nums)):
            for cap in range(target, nums[item]-1, -1):
                if cap == nums[item]:
                    return True
                cache[cap] = max(cache[cap], nums[item] + cache[cap-nums[item]])

        return False
