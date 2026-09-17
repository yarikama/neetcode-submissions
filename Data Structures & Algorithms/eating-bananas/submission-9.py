from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate, max_rate = 1, max(piles)

        if h == len(piles): return max_rate

        def canFinish(rate: int) -> bool:
            hrs = 0
            for pile in piles:
                hrs += ceil(pile / rate)
                if hrs > h: return False
            return True

        # if there is a plateau, we just left it. Also, we want to see which neighbor (min/max) we want. If whatever can be the answer, we are able to use == 0 to return. Otherwise, keep shrink the searching space. 

        ans = max_rate
        while min_rate <= max_rate:
            rate = (min_rate + max_rate) // 2

            if canFinish(rate):
                ans = rate
                max_rate = rate - 1
            else:
                min_rate = rate + 1

        return ans