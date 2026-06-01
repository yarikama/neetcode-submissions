class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = []
        total = 0
        for num in nums:
            total += num
            prefix_sum.append(total)

        print(prefix_sum)

        return 1