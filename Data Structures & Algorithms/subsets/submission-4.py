class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(idx: int, comb: List[int]) -> None:
            if idx >= len(nums):
                return

            if idx != -1:
                comb.append(nums[idx])

            res.append(comb)

            for i in range(idx+1, len(nums)):
                new_comb = comb[:]
                helper(i, new_comb)

        helper(-1, [])

        return res