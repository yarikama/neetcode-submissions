from heapq import *

class Solution:
    def jump(
        self, 
        nums: List[int]
    ) -> int:
        heap = [0]
        steps = 0
        while heap:
            i = -1 * heappop(heap)
            steps += 1
            for j in range(1, nums[i]+1):
                if i+j+nums[j] >= len(nums)-1:
                    return steps+1
                heappush(heap, -(i+j+nums[j]))
        return steps
                
        