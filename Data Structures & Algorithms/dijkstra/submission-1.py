from heapq import heappush, heappop

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {}

        for node in range(n):
            adj[node] = []

        for s, d, w in edges:
            adj[s].append((d, w))

        shortest_path = {}
        min_heap = [(0, src)]
        while min_heap:
            weight, node = heappop(min_heap)
            if node in shortest_path:
                continue
            shortest_path[node] = weight

            for dst, dst_weight in adj[node]:
                if dst in shortest_path:
                    continue
                heappush(min_heap, (weight + dst_weight, dst))

        for node in range(n):
            if node not in shortest_path:
                shortest_path[node] = -1

        return shortest_path
