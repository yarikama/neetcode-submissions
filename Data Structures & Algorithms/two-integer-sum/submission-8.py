class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {num: idx for idx, num in enumerate(nums)}

        res = []
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in cache and cache[diff] != idx:
                return [idx, cache[diff]]

        return []
        