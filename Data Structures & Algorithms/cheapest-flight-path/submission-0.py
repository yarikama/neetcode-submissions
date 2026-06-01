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

        total_cost = 0
        heap = [(0, src)]
        visited = set()

        while heap:
            cur_cost, node = heappop(heap)
            print(node)
            for cost, dst in adj[node]:
                if dst in visited:
                    continue
                heappush(heap, (cur_cost + cost, dst))
            total_cost = cur_cost
            visited.add(node)
        return total_cost
                

            


        