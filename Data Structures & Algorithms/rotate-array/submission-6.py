from math import gcd

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        for i in range(gcd(k,n)):
            prev = nums[i]
            nxt = i + k
            while nxt % n != i:
                nums[nxt % n], prev = prev, nums[nxt % n]
                nxt += k
            nums[i] = prev

