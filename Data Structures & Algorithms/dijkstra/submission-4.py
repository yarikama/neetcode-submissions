from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))

        shortest_path = {}
        min_heap = [(0, src)]
        while min_heap:
            w1, n1 = heappop(min_heap)
            if n1 in shortest_path:
                continue
            shortest_path[n1] = w1

            for n2, w2 in adj[n1]:
                heappush(min_heap, (w1+w2, n2))
        for i in range(n):
            if i not in shortest_path:
                shortest_path[i] = -1
        return shortest_path
