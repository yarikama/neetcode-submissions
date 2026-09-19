"""
nums = [2,3,1,5,4], k = 2

5 - 2
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k = n - k

        def quick_select(start: int, end: int) -> int:
            pivot = start
            
            for i in range(start, end):
                if nums[i] < nums[end]:
                    nums[pivot], nums[i] = nums[i], nums[pivot]
                    pivot += 1
            
            nums[pivot], nums[end] = nums[end], nums[pivot]

            if pivot == k:
                return nums[pivot]
            elif pivot < k:
                return quick_select(pivot + 1, end)
            else:
                return quick_select(start, pivot - 1)

        return quick_select(0, n-1)