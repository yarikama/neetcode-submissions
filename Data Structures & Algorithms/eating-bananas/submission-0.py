import math

class Solution:
    def minEatingSpeed(
        self, 
        piles: List[int], 
        h: int
    ) -> int:
        self.piles = piles
        self.h = h
        L, R = max(math.ceil(sum(piles)/h), 2), math.ceil(max(piles)/h) * len(piles)

        while(L <= R):
            M = (L + R)//2
            previous_result = self.eatup(M-1)
            result = self.eatup(M)
            print(f"Rate: {M}, Prev: {previous_result}, Now: {result}")
            if not previous_result and not result:
                L = M + 1
            if previous_result and result:
                R = M - 1
            elif previous_result is False and result is True:
                return M

        return 1

    def eatup(self, rate: int) -> bool:
        hours = 0
        for pile in self.piles:
            hours += math.ceil(pile/rate)

        print(f"hours: {hours}")
        return hours <= self.h


