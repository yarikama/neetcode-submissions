# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        L, R = 1, n
        while(L <= R):
            M = (L + R)//2
            result = guess(M)
            print(M)
            print(result)
            if result == -1:
                R = M-1
            elif result == 1:
                L = M+1
            elif result == 0:
                return M

        return M