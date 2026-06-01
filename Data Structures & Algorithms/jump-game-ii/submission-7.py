from heapq import *

class Solution:
    def jump(
        self, 
        nums: List[int]
    ) -> int:
        if len(nums) == 1:
            return 0

        steps = 0
        i = 0
        while i < len(nums)-2:
            steps += 1
            max_step = 0
            for j in range(1, nums[i]+1):
                if i+j >= len(nums)-1:
                    return steps
                max_step = max(max_step, i + j + nums[j])
            i = max_step
        return steps + 1


                
        