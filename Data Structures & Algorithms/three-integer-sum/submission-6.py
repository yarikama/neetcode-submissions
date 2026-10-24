class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        def twoSum(start, target) -> Tuple[int, int]:
            L, R = start, len(nums)-1
            while L < R:
                if nums[L] + nums[R] < target:
                    L += 1
                elif nums[L] + nums[R] > target:
                    R -= 1
                else:
                    res.add((-target, nums[L], nums[R]))
                    L += 1
                    R -= 1

        for idx, num in enumerate(nums[:-2]):
            twoSum(idx+1, -num)

        return list(res)