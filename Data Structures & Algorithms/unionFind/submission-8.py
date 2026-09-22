class UnionFind:
    
    def __init__(self, n: int):
        self.cnt = n
        self.par = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n
        
    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        self.cnt -= 1

        if self.rank[px] < self.rank[py]:
            px, py = py, px

        self.par[py] = px
        self.size[px] += self.size[py]

        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1

        return True


    def getNumComponents(self) -> int:
        return self.cnt

    def getUnionSize(self, x: int) -> int:
        return self.size[self.find(x)]

    def getUnionRank(self, x: int) -> int:
        return self.rank[self.find(x)]