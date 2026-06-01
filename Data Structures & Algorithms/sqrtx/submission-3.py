class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low < high:
            mid = int((low + high) / 2)
            result = self.check(x, mid)
            if result == 0:
                return mid
            elif result == 1:
                high = mid - 1
            elif result == -1:
                low = mid + 1  
        return low

    def check(self, x: int, div: int) -> int:
        product = div * div
        product_min = (div + 1) * (div + 1)
        if product == x:
            return 0
        if product < x and product_min > x:
            return 0
        if product > x:
            return 1
        if product < x:
            return -1


        