class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_cnts = [0, 0, 0]
        for color in nums:
            color_cnts[color] += 1

        i = 0
        for color in range(len(color_cnts)):
            while color_cnts[color] > 0:
                nums[i] = color
                color_cnts[color] -= 1
                i += 1