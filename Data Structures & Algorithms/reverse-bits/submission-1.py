class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_num = 0
        for i in range(32):
            if n & 1:
                reverse_num += (2 ** (31-i))
            n = n >> 1
        return reverse_num

        