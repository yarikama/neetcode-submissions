from typing import Set

class Graph:
    
    def __init__(self):
        g = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in g:
            g[src] = []        
        if dst not in g:
            g[dst] = []
        g[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        g[src].remove(dst)

    def hasPath(self, src: int, dst: int) -> bool:
        
        
        def dfs(node: int, target: int, visit: Set):
            if node in visit:
                return False

            if node == target:
                return True

            visit.add(node)
            for adj_node in g[node]:
                if dfs(adj_node, target, visit):
                    return True

            visit.remove(node)
            return False

        return dfs(node=src, target=dst, visit=set())