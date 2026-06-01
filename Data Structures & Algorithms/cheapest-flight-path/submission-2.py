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
            step, cur_cost, node = heappop(heap)
            for cost, dst in adj[node]:
                if dst in visited:
                    continue
                heappush(heap, (step+1, cur_cost + cost, dst))
            if node == dst:
                return cur_cost
            visited.add(node)
        return -1
            


        