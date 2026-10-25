class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def twoSum(start, target) -> None:
            L, R = start, len(nums)-1
            while L < R:
                if nums[L] + nums[R] < target:
                    L += 1
                elif nums[L] + nums[R] > target:
                    R -= 1
                else:
                    res.append((-target, nums[L], nums[R]))
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1

        for idx, num in enumerate(nums[:-2]):
            if nums[idx] > 0:
                break

            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            twoSum(idx+1, -num)

        return res