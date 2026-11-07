class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        
        cache = {}
        def get(x: int) -> int:
            if x in cache:
                return cache[x]

            ans = mountainArr.get(x)
            cache[x] = ans
            return ans

        # find peak
        L, R = 1, n-2
        while L <= R:
            mid = (L + R) // 2
            if get(mid-1) < get(mid) and get(mid) > get(mid + 1):
                break
            elif get(mid-1) < get(mid) < get(mid+1):
                L = mid + 1
            else:
                R = mid - 1

        peak = mid

        # search on left part
        L, R = 0, peak
        while L <= R:
            mid = (L + R) // 2
            if get(mid) == target:
                return mid
            elif get(mid) > target:
                R = mid - 1
            else:
                L = mid + 1

        L, R = peak+1, n-1
        while L <= R:
            mid = (L + R) // 2
            if get(mid) == target:
                return mid
            elif get(mid) > target:
                L = mid + 1
            else:
                R = mid - 1

        return -1

















        