from heapq import heappop, heappush

class Solution:
    def maxProbability(
        self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int
    ) -> float:

        adj = {}
        for i in range(n):
            adj[i] = []

        for edge, prob in zip(edges, succProb):
            src, dst = edge
            adj[src].append((prob, dst))
            adj[dst].append((prob, src))

        shortest_path = {}
        pq = [(-1, start_node)]
        while pq:
            prob, node = heappop(pq)
            prob *= -1

            if node in shortest_path:
                continue

            shortest_path[node] = prob

            for n_prob, n_node in adj[node]:
                if n_node in shortest_path:
                    continue

                heappush(pq, ((-1*(prob) * n_prob), n_node))

        if end_node not in shortest_path:
            return 0

        return shortest_path[end_node]


            




        