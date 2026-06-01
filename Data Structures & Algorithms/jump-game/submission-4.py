class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False

        L = 0
        while L + nums[L] < len(nums)-1:
            steps = [nums[L + i] + i for i in range(1, nums[L]+1) ]
            if not steps: return False
            new_L = max(steps)
            if L == new_L: return False
            L = new_L
            if L > len(nums)-1: break

        return True