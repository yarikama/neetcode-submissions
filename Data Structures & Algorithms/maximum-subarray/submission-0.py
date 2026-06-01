class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur_sum = 0
        max_sum = -1001

        for i in nums:
            cur_sum = max(i, cur_sum + i);
            max_sum = max(max_sum, cur_sum)

        return max_sum