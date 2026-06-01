class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        groups = [0, 0, 0]

        for i in nums:
            groups[i] += 1

        l = 0
        for index, individual_num in enumerate(groups):
            for individual in range(individual_num):
                nums[l] = index
                l += 1
        