class Solution:
    def reverseBits(self, n: int) -> int:
        l = []
        while n:
            l.append(1 if n & 1 else 0)
            n = n << 1
        print(l)
        return n

        