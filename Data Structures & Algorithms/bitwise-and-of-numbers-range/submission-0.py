"""
001

010
011
100

101
---------
1010

1011

1100
"""


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right - 1
        return right

        

        