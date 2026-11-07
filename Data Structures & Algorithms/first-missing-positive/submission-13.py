class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            # skip
            if not 1 <= nums[i] <= n:
                continue
        
            j, val = i, -1
            while nums[j] != j + 1:
                val, nums[j] = nums[j], val
                
                # skip
                if not 1 <= val <= n:
                    break
                
                j = val - 1

        # validation
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1