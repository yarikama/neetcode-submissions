class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        prev, curr = 0, 0
        for i in range(1, len(nums)):
            nums[i] += max(prev, curr)
            prev = curr
            curr = nums[i-1]

        return max(nums[-1], nums[-2])