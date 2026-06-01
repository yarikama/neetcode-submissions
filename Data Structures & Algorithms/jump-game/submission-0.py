class Solution:
    def canJump(self, nums: List[int]) -> bool:
        L = 0
        while L + nums[L] < len(nums)-1:
            steps = [nums[L + i] + i for i in range(1, nums[L]+1) ]
            new_L = max((*steps, 0))
            if new_L == 0:
                return False
            L = new_L

        return True