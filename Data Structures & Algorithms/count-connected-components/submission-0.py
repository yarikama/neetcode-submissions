class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parent = {}
        self.rank = {}
        self.n = n
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
        
        for x, y in edges:
            self.union(x, y)
            self.union(y, x)

        return self.n

    def union(self, x: int, y: int) -> None:
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        
        self.n -= 1
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return

    def find(self, x: int) -> int:
        cur = self.parent[x]
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur


        