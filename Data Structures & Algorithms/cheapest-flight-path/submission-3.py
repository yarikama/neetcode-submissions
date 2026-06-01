from collections import defaultdict
from heapq import *

class Solution:
    def findCheapestPrice(
        self, 
        n: int, 
        flights: List[List[int]], 
        src: int, 
        dst: int, 
        k: int
    ) -> int:
        adj = defaultdict(list)

        for n1, n2, price in flights:
            adj[n1].append((price, n2))

        heap = [(0, 0, src)]
        visited = set()

        while heap:
            cur_cost, step, node = heappop(heap)
            if step > k+1:
                continue

            for cost, dst in adj[node]:
                if dst in visited:
                    continue
                heappush(heap, (cur_cost + cost, step+1, dst))

            if node == dst:
                return cur_cost

            visited.add(node)
        return -1
            


        