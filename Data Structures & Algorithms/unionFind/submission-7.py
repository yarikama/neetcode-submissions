class UnionFind:
    
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank_upper_bound = [0 for _ in range(n)]
        self.cnt = n

    def find(self, x: int) -> int:
        p = self.parent[x]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p        

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        self.cnt -= 1
        rx, ry = self.rank_upper_bound[px], self.rank_upper_bound[py]
        if rx > ry:
            self.parent[py] = px
        elif rx < ry:
            self.parent[px] = py
        else:
            self.parent[px] = py
            self.rank_upper_bound[py] += 1
        return True
        
    def getNumComponents(self) -> int:
        return self.cnt
