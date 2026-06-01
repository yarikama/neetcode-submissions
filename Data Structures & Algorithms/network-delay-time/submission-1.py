from heapq import heappop, heappush

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = {}

        for i in range(1, n+1):
            adj[i] = []

        for ui, vi, ti in times:
            adj[ui].append((ti, vi))

        sp = {}
        pq = [(0, k)]
        while pq:
            t1, n1 = heappop(pq)
            if n1 in sp:
                continue
            sp[n1] = t1

            for t2, n2 in adj[n1]:
                if n2 in sp:
                    continue
                heappush(pq, (t1+t2, n2))


        res = sp[k]
        for i in range(1, n+1):
            if i not in sp:
                return -1
            res = max(res, sp[i])

        return res


        