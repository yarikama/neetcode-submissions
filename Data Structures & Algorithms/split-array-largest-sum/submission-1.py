import bisect

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isSeparable(seg: int, k: int):
            sum = 0
            total = 1

            for num in nums:
                sum += num
                if sum > seg:
                    sum = num
                    total += 1

            return total <= k


        L, R = max(nums), sum(nums)
        while L <= R:
            mid = (L + R) // 2
            if isSeparable(mid, k):
                R = mid - 1
            else:
                L = mid + 1

        return L
            


            
            