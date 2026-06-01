from heapq import heappop, heappush
from functools import reduce

class UnionFind:
    def __init__(self, n: int):
        self.rank, self.parent = {}, {}
        for i in range(n):
            self.rank[i] = 0
            self.parent[i] = i

    def find(self, n: int) -> int:
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] > self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True
    

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        min_heap = []
        for u, v, w in edges:
            heappush(min_heap, (w, u, v))

        print(min_heap)

        mst = []
        union_find = UnionFind(n)
        while len(mst) < n-1:
            w, u, v = heappop(min_heap)
            if not union_find.union(u, v):
                continue
            mst.append((w, v))
        return sum(i[0] for i in mst)
        

        











