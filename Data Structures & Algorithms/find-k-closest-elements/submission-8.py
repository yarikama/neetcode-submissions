import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect.bisect_left(arr, x)

        if idx == 0:
            L, R = -1, 0
        else:
            L, R = idx - 1, idx

        while L >= 0 and R < len(arr) and R - L - 1 < k:
            diff_L, diff_R = abs(arr[L] - x), abs(arr[R] - x)
            if diff_L <= diff_R:
                L -= 1
            else:
                R += 1

        while L >= 0 and R - L - 1 < k:
            L -= 1

        while R < len(arr) and R - L - 1 < k:
            R += 1

        return arr[L+1:R]