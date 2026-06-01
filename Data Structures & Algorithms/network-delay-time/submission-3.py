from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def networkDelayTime(
        self, times: List[List[int]], n: int, k: int
    ) -> int:

        # construct the graph using default dict
        adj = defaultdict(list)

        for u, v, time in times:
            adj[u].append((v, time))

        # init the data structure
        sp = {}
        pq = [(0, k)]

        while pq:
            # choose the smallest value every time
            n, time = heappop(pq)

            if n in sp:
                continue

            sp[n] = time

            for nn, time2 in adj[n]:
                pq.heappush(nn, time + time2)

            
        res = sp[k]

        for i in range(1, n+1):
            if i not in sp:
                return -1
            res = max(res, sp[i])
        

        return res
