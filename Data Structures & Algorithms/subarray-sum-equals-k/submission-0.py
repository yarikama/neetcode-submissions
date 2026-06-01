class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      result = 0
      cur_sum = 0
      prefix_sum = {0 : 1}

      for num in nums:
        cur_sum += num
        diff = cur_sum - k

        result += prefix_sum.get(diff, 0)
        prefix_sum[cur_sum] = 1 + prefix_sum.get(cur_sum, 0)

      return result 