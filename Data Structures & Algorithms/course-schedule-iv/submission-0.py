from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for src, dst in prerequisites:
            adj[src].append(dst)

        visit, path = set(), set()
        index = 0
        topo_sort = defaultdict(int)

        def dfs(node: int, index: int) -> bool:
            if node in visit: return False
            if node in path: return True

            path.add(node)

            for dst in adj[node]:
                if dfs(dst, index+1): return True

            path.remove(node)
            visit.add(node)
            topo_sort[index] = node

        for i in range(numCourses):
            if dfs(i, 0): return [False] * len(queries)

        print(topo_sort)

        return [topo_sort[src] <= topo_sort[dst] for src, dst in queries]
            
            
        