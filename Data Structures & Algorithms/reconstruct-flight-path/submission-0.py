from collections import defaultdict
from heapq import *

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(set)
        for idx, (src, dst) in enumerate(tickets):
            adj[src].add((idx+1, dst)) # price, dst

        ans = []
        heap = [(0, 'JFK')]
        while heap:
            cost, src = heappop(heap)
            for price, dst in adj[src]:
                heappush(heap, (cost + price, dst))
            adj[src] = set()
            ans.append(src)
        return ans


        