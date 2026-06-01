from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                wgt = abs(x2 - x1) + abs(y2 - y1)
                adj[(x1, y1)].append((wgt, x2, y2))

        total_cost = 0
        visit = set()
        visit.add(tuple(points[0])) # Be careful with these, can't be written as set(tuple(points[0])), must use set.add()
        min_heap = []
        for wgt, x, y in adj[tuple(points[0])]:
            heappush(min_heap, (wgt, x, y))
   
        while min_heap:
            wgt1, x1, y1 = heappop(min_heap)
            if (x1, y1) in visit:
                continue

            visit.add((x1, y1))
            total_cost += wgt1

            for wgt2, x2, y2 in adj[(x1, y1)]:
                if (x2, y2) not in visit:
                    heappush(min_heap, (wgt2, x2, y2))

        return total_cost