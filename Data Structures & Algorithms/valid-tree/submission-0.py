class UnionFind:
    def __init__(self, n: int):
        self.parent = [ i for i in range(n) ]
        self.rank = [ 0 for _ in range(n) ]
        self.cnt = n

    def find(self, node: int) -> int:
        parent = self.parent[node]
        while parent != self.parent[parent]:
            self.parent[parent] = self.parent[self.parent[parent]]
            parent = self.parent[parent]
        return parent

    def union(self, node1: int, node2: int) -> bool:
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2: return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1

        self.cnt -= 1
        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        unionFind = UnionFind(n)
        for src, dst in edges:
            if not unionFind.union(src, dst):
                return False

        return unionFind.cnt == 1
