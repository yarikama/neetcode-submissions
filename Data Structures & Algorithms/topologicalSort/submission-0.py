from collections import defaultdict

class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        self.visit, self.adj, self.topologic_sort, self.path = set(), defaultdict(list), [], set()

        for src, dst in edges:
            self.adj[src].append(dst)

        for node in range(n):
            if self.dfs(node):
                return []
        
        return self.topologic_sort[::-1]

    def dfs(self, node: int) -> bool:
        if node in self.visit:
            return False
        if node in self.path:
            return True

        self.visit.add(node)
        self.path.add(node)

        for dst in self.adj[node]:
            if dst in self.path:
                return True
            if self.dfs(dst):
                return True

        self.path.remove(node)
        self.topologic_sort.append(node)
        return False