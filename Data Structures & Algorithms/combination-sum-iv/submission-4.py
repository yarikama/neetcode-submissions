class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def backtrack(curr_sum: int):
            if curr_sum == target:
                return 1

            if curr_sum > target:
                return 0

            if curr_sum in memo:
                return memo[curr_sum]

            ans = 0
            for num in nums:
                ans += backtrack(curr_sum + num)

            memo[curr_sum] = ans

            return ans

        return backtrack(0)