class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                want = target - nums[i] - nums[j]
                L, R = j + 1, len(nums)-1

                while L < R:
                    if nums[L] + nums[R] > want:
                        R -= 1
                    elif nums[L] + nums[R] < want:
                        L += 1
                    else:
                        res.append((nums[i], nums[j], nums[L], nums[R]))
                        L += 1
                        R -= 1
                        while L < R and nums[L] == nums[L-1]:
                            L += 1

        return res


