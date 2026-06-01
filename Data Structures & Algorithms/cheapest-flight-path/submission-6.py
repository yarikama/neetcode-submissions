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
        ans = {}
        while heap:
            cur_cost, step, node = heappop(heap)
            if step > k+1:
                continue

            for cost, dst in adj[node]:
                if dst in ans and ans[dst] < cur_cost + cost:
                    continue
                print( (cur_cost + cost, step+1, dst))
                heappush(heap, (cur_cost + cost, step+1, dst))
            if cur_cost == 200:
                print(cur_cost, node) 

            ans[node] = cur_cost
            if node == dst:
                return ans[node]

        return ans[dst] if dst in ans else -1
            


        