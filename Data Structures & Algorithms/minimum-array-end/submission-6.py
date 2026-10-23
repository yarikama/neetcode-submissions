class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        n -= 1
        bit = 1
        while n:
            if not (x & bit):
                res |= (n & 1) * bit
                n >>= 1
            bit <<= 1
        return res