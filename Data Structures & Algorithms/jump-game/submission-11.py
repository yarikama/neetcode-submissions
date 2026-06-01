from heapq import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False

        def dfs(idx: int) -> int:
            if idx >= len(nums)-1:
                return idx

            max_step = nums[idx]
            result = max_step + idx
            # Base Case
            if result >= len(nums) - 1:
                return result

            for i in range(1, max_step+1):
                result = max(result, dfs(idx + nums[idx+i] + i))

            return result                



        return dfs(0) >= len(nums) - 1