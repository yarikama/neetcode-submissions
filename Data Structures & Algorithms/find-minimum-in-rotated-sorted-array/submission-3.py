class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums)-1

        while L <= R:
            mid = (R + L) // 2
            # if mid == len(nums) - 1:
                # return nums[0] 
            if nums[mid] < nums[mid-1] and nums[mid] < nums[mid+1]:
                return nums[mid]
            elif nums[mid] < nums[0]:
                R = mid -1
            else:
                L = mid +1 

        return nums[0]
        