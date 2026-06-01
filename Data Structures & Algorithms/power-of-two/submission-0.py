class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        L, R = 0, 32

        while L <= R:
            mid = int((R + L) / 2)
            result = self.check(n, mid)

            if result == 1:
                return True

            elif result == 0:
                R = mid - 1 
            
            else:
                L = mid + 1

        return False


    def check(self, n: int, bits: int) -> int:
        comp = 2 ** bits
        if comp > n:
            return 0
        elif comp == n:
            return 1
        else:
            return 2
        