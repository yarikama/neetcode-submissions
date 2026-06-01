from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        SRC = 0
        NO_SOLUTION = -1

        # Undirected Graph
        adj = defaultdict(list)
        for src, dst, wgt in edges:
            adj[src].append((wgt, dst))
            adj[dst].append((wgt, src))

        # Init Min Heap, Visit, Total Cost
        total_cost = 0
        visit = set([SRC])
        min_heap = []
        for wgt, dst in adj[SRC]:
            heappush(min_heap, (wgt, dst))

        # Prim's Algor.
        while min_heap:
            wgt, dst = heappop(min_heap)
            # Base Case
            if dst in visit:
                continue

            visit.add(dst)
            total_cost += wgt
            for wgt1, dst1 in adj[dst]:
                if dst1 not in visit:
                    heappush(min_heap, (wgt1, dst1))

        return total_cost if len(visit) == n else NO_SOLUTION
            
