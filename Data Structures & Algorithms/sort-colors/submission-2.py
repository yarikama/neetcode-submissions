class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0] * 3

        for num in nums:
            colors[num] += 1

        x = 0
        for color in range(len(colors)):
            for i in range(colors[color]):
                nums[x] = color
                x += 1
