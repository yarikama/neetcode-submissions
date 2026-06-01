class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        while n:
            l.append(1 if n & 1 else 0)
            n = n >> 1
        return l
        