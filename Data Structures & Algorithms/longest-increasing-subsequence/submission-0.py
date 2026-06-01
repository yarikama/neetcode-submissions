class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(i: int, largest: int) -> int:
            if i >= len(nums):
                return 0

            # Skip
            skip = dfs(i+1, largest)

            # include
            if largest < nums[i]:
                include = 1 + dfs(i+1, nums[i])
            else:
                include = 0

            return max(skip, include)

        return dfs(0, float('-inf'))