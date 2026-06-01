class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_sum, max_sum = 0, nums[0]
        max_L, max_R, L = 0, 0, 0
        nums *= 2

        for R in range(len(nums)):
            if R - len(nums)/2 >= L:
                cur_sum -= nums[L]
                L += 1 

            if cur_sum < 0:
                L = R
                cur_sum = 0

            cur_sum += nums[R]


            if cur_sum > max_sum:
                max_sum = cur_sum
                max_L, max_R = L, R

            
        return max_sum


        