class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b & mask:
            carry = ((a & b) << 1) & mask # Carry AND
            a = (a ^ b) & mask # Sum XOR
            b = carry

        return a if a <= max_int else ~(a ^ mask)

            