class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_sum, max_sum = 0, nums[0]
        max_L, max_R= 0, 0
        len_num = len(nums)
        nums += nums

        L = 0
        for R in range(len(nums)):
            cur_sum += nums[R]
            if R - L + 1 > len_num:
                cur_sum -= nums[L]
                L += 1
                while (cur_sum > cur_sum - nums[L] and L <= R):
                    cur_sum -= nums[L]
                    L += 1


            if cur_sum < 0:
                cur_sum = 0
                L = R 

            if max_sum < cur_sum:
                max_sum = cur_sum
                max_L, max_R = L, R

        return max_sum


        