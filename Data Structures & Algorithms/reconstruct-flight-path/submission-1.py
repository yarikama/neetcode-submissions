from collections import defaultdict
from heapq import *

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(set)
        for idx, (src, dst) in enumerate(tickets):
            adj[src].add((idx+1, dst)) # price, dst

        ans = []
        heap = [(0, 'JFK', -1, -1)]
        i = 0
        while heap and i <= len(tickets):
            cost, src, last_src, org_cost = heappop(heap)
            if (org_cost, src) in adj[last_src]:
                adj[last_src].remove((org_cost, src))
            heap = []
            for price, dst in adj[src]:
                heappush(heap, (cost + price, dst, src, price))
            ans.append(src)
            i += 1
        return ans


        