class UnionFind:
    
    def __init__(self, n: int):
        self.n = n
        self.parent = {}
        self.rank = {}

        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        cur = self.parent[x]
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def isSameComponent(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return True
        return False

    def union(self, x: int, y: int) -> bool:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[y] = root_x
        else:
            self.parent[x] = root_y
            self.rank[root_y] += 1

        return True
        

    def getNumComponents(self) -> int:
        s = set()
        for i in self.parent:
            s.add(self.find(i))

        return len(s)
