class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        def dfs(i: int, amount: int) -> int:
            if i >= len(nums):
                return amount
                
            skip = dfs(i+1, 1)
            include = dfs(i+1, amount * nums[i])

            return max(skip, include)

        return dfs(0, 1)
        