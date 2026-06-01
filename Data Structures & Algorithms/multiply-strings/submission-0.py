class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.toInt(num1) * self.toInt(num2))

    def toInt(self, num: str) -> int:
        return sum( 10 ** idx * int(digit) for idx, digit in enumerate(num[::-1]) )

        