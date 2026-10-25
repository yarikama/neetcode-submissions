class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []

        def helper(i: int = 0, curr_xor: int = 0) -> None:
            if i > len(nums)-1:
                return 

            curr_xor ^= nums[i]
            res.append(curr_xor)
            helper(i+1, curr_xor)
            curr_xor ^= nums[i]
            helper(i+1, curr_xor)

        helper()
        return sum(res)
