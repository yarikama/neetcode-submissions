class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        L, R = 0, len(nums)

        while L < R:
            if nums[L] != val:
                L += 1
            else:
                R -= 1
                nums[L] = nums[R]

        return L


        