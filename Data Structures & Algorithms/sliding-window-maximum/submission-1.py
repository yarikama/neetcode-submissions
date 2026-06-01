from heapq import *

class Solution:
    def maxSlidingWindow(
        self, 
        nums: List[int], 
        k: int,
    ) -> List[int]:
        if len(nums) < k:
            return []

        rst = []
        heap = []
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                if nums[R] > -1 * nsmallest(1, heap)[0]:
                    heap = []
                L += 1

            heappush(heap, -nums[R])

            if R >= k-1:
                rst.append(-1 * nsmallest(1, heap)[0])

        return rst

            
        
        