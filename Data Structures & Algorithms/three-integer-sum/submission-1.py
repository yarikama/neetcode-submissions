class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        idx = 0
        while idx < len(nums)-2:
            num = nums[idx]
            target = -num
            L, R = idx+1, len(nums)-1

            while L < R:
                diff = nums[L] + nums[R]
                if diff == target:
                    comb = [num, nums[L], nums[R]]
                    res.append(comb)
                    while nums[L] == nums[L+1]:
                        L += 1
                    while nums[R] == nums[R-1]:
                        R -= 1
                    while nums[idx] == nums[idx+1]:
                        idx += 1

                    L += 1
                    R -= 1
                    idx += 1

                elif diff > target:
                    R -= 1
                else:
                    L += 1

            idx += 1

        return res
                

                
