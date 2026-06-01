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

        # Dijkstra
        shortest_path = {}
        heap = [(0, 0, src)] # Price, Step, destination
        while heap:
            price, step, src = heappop(heap)
            if src in shortest_path:
                continue
            if step > k + 1:
                continue
            for price_to_add, dst in adj[src]:
                heappush(heap, (price + price_to_add, step + 1, dst))

            shortest_path[src] = price

        return shortest_path[dst] if dst in shortest_path else -1
            


                