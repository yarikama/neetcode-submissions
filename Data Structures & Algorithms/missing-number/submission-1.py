class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        l = l * (l + 1) // 2
        for num in nums:
            l -= num
        return l 
        