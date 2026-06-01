from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((w, v))
            adj[v].append((w, u))

        pq = [(0, 0)]
        visited = set()
        total_cost = 0

        while pq:
            w1, v1 = heappop(pq)
            if v1 in visited:
                continue

            total_cost += w1
            visited.add(v1)

            for w2, v2 in adj[v1]:
                heappush(pq, (w2, v2))

        return total_cost if len(visited) == n else -1
            
