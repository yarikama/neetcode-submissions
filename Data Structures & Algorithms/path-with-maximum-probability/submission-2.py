from heapq import heappop, heappush

class Solution:
    def maxProbability(
        self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int
    ) -> float:

        adj = {}
        for i in range(n):
            adj[i] = []
        
        for i in range(len(edges)):
            ui, vi = edges[i]
            wi = succProb[i]
            adj[ui].append((wi, vi))
            adj[vi].append((wi, ui))

        sp, pq = {}, [(-1, start_node)]
        while pq:
            ti, ni = heappop(pq)
            if ni in sp:
                continue
            sp[ni] = ti

            for tj, nj in adj[ni]:
                if nj in sp:
                    continue
                heappush(pq, (tj * ti, nj))


        return -1*sp.get(end_node, 0)


            




        