class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            sum_1_bits = 0
            while i:
                l.append(1 if i & 1 else 0)
                i = i >> 1
        return l
        