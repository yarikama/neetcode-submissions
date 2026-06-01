class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # init
        self.parent = {}
        self.rank = {}
        n = len(edges) + 1
        for i in range(1, n+1):
            self.parent[i] = i
            self.rank[i] = 0

        ans = None
        for x, y in edges:
            root_x, root_y = self.find(x), self.find(y)
            if root_x == root_y:
                ans = [x, y] # get the last cyclic edge
            else:
                self.union(root_x, root_y)
        return ans
        
    def find(self, x: int) -> bool:
        cur = self.parent[x]
        while cur != self.parent[cur]:
            self.parent[cur] = self.parent[self.parent[cur]]
            cur = self.parent[cur]
        return cur

    def union(self, root_x: int, root_y: int) -> None:
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_x] = root_y
            self.rank[root_y] += 1


