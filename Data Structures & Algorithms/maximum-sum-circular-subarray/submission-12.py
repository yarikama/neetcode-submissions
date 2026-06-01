class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        g_min, g_max = nums[0], nums[0]
        l_min, l_max = 0, 0
        total = 0

        for num in nums:
            l_min = min(l_min + num, num)
            l_max = max(l_max + num, num)

            total += num

            g_min = min(l_min, g_min)
            g_max = max(l_max, g_max)

        return max(g_max, total - g_min) if g_max > 0 else g_max

        