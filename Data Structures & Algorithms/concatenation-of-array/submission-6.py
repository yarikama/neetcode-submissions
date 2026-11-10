class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # # Solution 1:
        # nums *= 2 
        # return nums

        # # Solution2:
        for i in range(len(nums)):
            nums.append(nums[i])

        return nums