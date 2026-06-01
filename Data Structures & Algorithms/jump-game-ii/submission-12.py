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
        while i < len(nums)-1:
            max_step = 0
            change_to = 0
            for j in range(1, nums[i]+1):
                if i+j >= len(nums)-1:
                    return steps + 1
                if i + j + nums[j] > max_step:
                    max_step = i + j + nums[j]
                    change_to = i + j
            i = change_to
            steps += 1


                
        