class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        res = []
        def helper(idx: int, target: int, comb: List[int]):
            if idx >= len(nums):
                return


            # to be 
            new_target = target - nums[idx]
            if new_target < 0:
                return

            new_comb = comb.copy() + [nums[idx]]
            if new_target == 0:
                res.append(new_comb)
                return

            if new_target > 0:
                helper(idx, new_target, new_comb)

            # or not to be
            helper(idx+1, target, comb)

        helper(0, target, [])
        return res

        

        