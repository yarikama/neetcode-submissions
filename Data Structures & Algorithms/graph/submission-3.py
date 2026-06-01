from typing import Set

class Graph:
    
    def __init__(self):
        self.g = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.g:
            self.g[src] = []        
        if dst not in self.g:
            self.g[dst] = []
        self.g[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if dst in self.g and src in self.g:
            self.g[src].remove(dst)
            return True

        return False

    def hasPath(self, src: int, dst: int) -> bool:
        
        
        def dfs(node: int, target: int, visit: Set) -> bool:
            if node in visit:
                return False

            if node == target:
                return True

            visit.add(node)
            for adj_node in self.g[node]:
                if dfs(adj_node, target, visit):
                    return True

            visit.remove(node)
            return False

        return dfs(node=src, target=dst, visit=set())