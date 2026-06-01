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
        topo_sort = {}
        
        def dfs(node: int, index: int) -> bool:
            if node in visit: return False
            if node in path: return True

            path.add(node)
            if any(dfs(dst, index+1) for dst in adj[node]): return True
            path.remove(node)

            visit.add(node)
            topo_sort[node] = index

        for i in range(numCourses):
            if dfs(i, -i): return [False for _ in range(numCourses)]
        
        print(topo_sort)
        minKey, minVal = -1, -1
        for key, val in topo_sort.items():
            if minVal > val:
                minKey, minVal = key, val

        visit.clear()
        path.clear()
        dfs(minKey, 0)
        print(topo_sort)

        return [ topo_sort[src] < topo_sort[dst] for src, dst in queries ]
            