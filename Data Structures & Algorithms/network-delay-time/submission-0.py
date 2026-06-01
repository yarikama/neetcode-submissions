from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = {}
        for i in range(1, n+1):
            adj[i] = []

        for ui, vi, ti in times:
            adj[ui].append((ti, vi))

        
        shortest_path = {}
        pq = [(0, k)]

        while pq:
            w1, n1 = heappop(pq)
            if n1 in shortest_path:
                continue
            shortest_path[n1] = w1

            for w2, n2 in adj[n1]:
                if n2 in shortest_path:
                    continue
                heappush(pq, (w1+w2, n2))

        max_len = 0
        for i in range(1, n+1):
            if i not in shortest_path:
                return -1
            max_len = max(max_len, shortest_path[i])

        return max_len