class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(
            nums[0], 
            self.helper(nums[1:]),
            self.helper(nums[:-1]),
        )

    def helper(self, nums: List[int]) -> int:
        curr, prev = 0, 0

        for num in nums:
            tmp = curr
            curr = max(
                curr,
                prev + num,
            )
            prev = tmp

        return curr