from heapq import heappop, heappush
from functools import reduce

class UnionFind:
    def __init__(self, n: int):
        self.rank, self.par = {}, {}

        for i in range(n):
            self.rank[i] = 0
            self.par[i] = i

    def find(self, n: int) -> int:
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2) 
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p2] += 1

        return True



class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        pq = []
        for u, v, w in edges:
            heappush(pq, (w, u, v))

        mst = []
        uf = UnionFind(n)
        while len(mst) < n-1:
            if not pq:
                return -1

            w, u, v = heappop(pq)

            if not uf.union(u, v):
                continue

            mst.append((w, u, v))

        return sum(w for w, _, _ in mst)
            
        

        











