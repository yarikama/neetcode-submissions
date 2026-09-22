from heapq import heappush, heappop, heappush_max, heapify, heapify_max, heappop_max

class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        cap_and_pros = [ (cap, pro) for cap, pro in zip(capital, profits) ]
        cap_and_pros.sort(key=lambda x: (x[0], -x[1]))

        ptr = 0

        n = len(profits)
        h = []

        j = 0
        for i in range(min(k, n)):
            while j < n and w >= cap_and_pros[j][0]:
                heappush_max(h, cap_and_pros[j][1])
                j += 1
            if h:
                w += heappop_max(h)
            
        return w
            


        