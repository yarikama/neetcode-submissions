class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n+1):
            sum_1_bits = 0
            while i:
                if i & 1:
                    sum_1_bits += 1
                i = i >> 1
            l.append(sum_1_bits)
        return l
        