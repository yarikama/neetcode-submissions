class Solution:
    def reverse(self, x: int) -> int:
        isNegative = True if x < 0 else False

        x = int(str(abs(x))[::-1])

        if isNegative:
            x *= -1

        if 2 ** 31 - 1 < x or x < -2 ** 31:
            return 0

        return x
        
        