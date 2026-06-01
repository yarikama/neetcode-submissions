class UnionFind:
    def __init__(self, n: int):
        self.pars = [ i for i in range(n) ]
        self.rank = [ 0 for _ in range(n) ]
        self.cnt = n

    def find(self, node: int) -> int:
        par = self.pars[node]
        while par != self.pars[par]:
            self.pars[par] = self.pars[self.pars[par]]
            par = self.pars[par]
        return par

    def union(self, node1: int, node2: int) -> bool:
        if (p1 := self.find(node1)) == (p2 := self.find(node2)):
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.pars[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.pars[p1] = p2
        else:
            self.pars[p1] = p2
            self.rank[p2] += 1
        self.cnt -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, 
        n: int, 
        edges: List[List[int]],
    ) -> List[List[int]]:
        # [src, dst, weight, index]
        for idx, edge in enumerate(edges):
            edge.append(idx)

        # Kruskal: Sorted by weight
        edges.sort(key=lambda x: x[2])

        # Kruskal: Pop out ascend from edges
        mst_wgt = 0
        union_find = UnionFind(n)
        for src, dst, wgt, idx in edges:
            if union_find.union(src, dst): mst_wgt += wgt # Run once to know the minimum cost of a MST

        # Two for-loops to skip or include current edge and construct MST
        critical_edges, pseudo_edges = [], []
        for src, dst, wgt, idx in edges:
            # Kruskal without this edge
            curr_wgt = 0
            union_find = UnionFind(n)
            
            for src1, dst1, wgt1, idx1 in edges:
                if idx1 == idx: continue
                if union_find.union(src1, dst1): curr_wgt += wgt1

            if union_find.cnt != 1 or curr_wgt > mst_wgt:
                critical_edges.append(idx)
                continue # Skip checking pseudos

            # Again
            curr_wgt = wgt
            union_find = UnionFind(n)
            union_find.union(src, dst)
            
            for src1, dst1, wgt1, idx1 in edges:
                if union_find.union(src1, dst1): curr_wgt += wgt1

            if curr_wgt == mst_wgt:
                pseudo_edges.append(idx)

        return [critical_edges, pseudo_edges]

            


























