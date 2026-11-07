class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                continue

            if nums[i] > len(nums):
                nums[i] = -1

            prev = -1
            while nums[i] != i+1:
                prev, nums[i] = nums[i], prev

                if prev <= 0:
                    break

                if prev > len(nums):
                    break

                i = prev - 1    

        for i in range(1, len(nums)+1):
            if i != nums[i-1]:
                return i

        return len(nums)+1




        
