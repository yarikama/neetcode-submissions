from collections import deque

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = deque()
        while columnNumber > 26:
            res.appendleft(chr((columnNumber % 26) + ord('A') - 1))
            columnNumber //= 26
        res.appendleft(chr(columnNumber + ord('A') - 1))
        return "".join(res)
