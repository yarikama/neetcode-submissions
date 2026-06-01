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
        # Create a graph
        adj = defaultdict(list)
        for from_i, to_i, price_i in flights:
            adj[from_i].append((price_i, to_i))

        shortest_path = {}
        heap = [(0, 0, src)] # Step, Price, destination
        while heap:
            step, price, src = heappop(heap)
            if step > k + 1:
                continue
            if src in shortest_path and shortest_path[src] < price:
                continue
            for price_to_add, destination in adj[src]:
                heappush(heap, (step + 1, price + price_to_add, destination))
            shortest_path[src] = price
        return shortest_path[dst] if dst in shortest_path else -1
            


                