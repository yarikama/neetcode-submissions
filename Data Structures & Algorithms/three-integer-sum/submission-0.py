class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for idx in range(len(nums)-2):
            num = nums[idx]
            target = -num

            L, R = idx+1, len(nums)-1
            while L < R:
                comb = [num]
                diff = nums[L] + nums[R]
                if diff == target:
                    comb.append(nums[L])
                    comb.append(nums[R])
                    res.append(comb)

                


