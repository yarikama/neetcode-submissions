class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        def dfs(i: int, amount: int) -> int:
            skip = dfs(i+1, 1) if i+1 < len(nums) else 0

            new_amount = amount * nums[i]
            include = dfs(i+1, new_amount) if i+1 < len(nums) else new_amount
            if i == 1:
                print(skip, include)
            return max(skip, include)

        return dfs(0, 1)
        