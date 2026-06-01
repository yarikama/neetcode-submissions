class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1


        def recur(x: float, n: int) -> float:
            if n == 1: return x

            value = recur(x, n // 2)
            
            if n % 2 == 0: return value * value
            
            return x * value * value

        value = recur(x, abs(n))

        return value if n > 0 else 1 / value

