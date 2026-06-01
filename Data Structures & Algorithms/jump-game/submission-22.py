class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False

        def mydfs(idx: int) -> int:
            if idx >= len(nums)-1: 
                return idx

            max_step = nums[idx]
            result = max_step + idx
            for i in range(1, max_step+1):
                if idx + i >= len(nums)-1: 
                    return idx + i
                    
                for j in range(1, nums[idx+i]+1): # FUCK THIS ONE
                    result = max(mydfs(idx + j + i), result)

            return result                

        return mydfs(0) >= len(nums) - 1