from collections import defaultdict

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = defaultdict(int)
        
        def dfs(nums) -> int:
            if nums in cache:
                return cache[nums]

            res = 0
            n = len(nums)
            for idx, num in enumerate(nums):
                prod = num
                if idx > 0:
                    prod *= nums[idx-1]
                if idx < n-1:
                    prod *= nums[idx+1]

                new_nums = nums[:idx] + nums[idx+1:]
                res = max(res, prod + dfs(new_nums))

            cache[nums] = res
            return res

        return dfs(tuple(nums))

                

        