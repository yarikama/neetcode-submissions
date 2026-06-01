# 想法：
# 一直加上 Carry 跟 Sum，只要 Carry 還沒變成 0 就持續跑動
# 因為 python 要處理無限大的數目，所以需要去 & 0xFFFFFFFF 來保證數目在 32 bits 中可以表達。
# 最後也需要確認是不是負數 （大於 max_int），然後將數字轉成負數

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b & mask:
            carry = ((a & b) << 1) & mask # Carry AND
            a = (a ^ b) & mask # Sum XOR
            b = carry

        return a if a <= max_int else ~(a ^ mask)

            