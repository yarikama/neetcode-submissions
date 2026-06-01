from collections import defaultdict


class Solution:
    def checkIfPrerequisite(self, 
        numCourses: int, 
        prerequisites: List[List[int]], 
        queries: List[List[int]]
    ) -> List[bool]:
        if not prerequisites: return [False for _ in range(numCourses)]

        adj = defaultdict(list)
        for src, dst in prerequisites:
            adj[src].append(dst)
        
        visit, path = set(), set()
        topo_sort = []
        
        ans = defaultdict(set)
        def dfs(node: int, index: int) -> bool:
            if node in visit: return False
            if node in path: return True

            path.add(node)
            if any(dfs(dst, index+1) for dst in adj[node]): return True
            path.remove(node)

            visit.add(node)
            ans[node] = set(topo_sort.copy())
            topo_sort.append(node)

        for i in range(numCourses):
            if dfs(i, -i): return [False for _ in range(numCourses)]

        
        return [bool(dst in ans[src]) for src, dst in queries]

            