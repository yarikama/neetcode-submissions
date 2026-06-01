from collections import defaultdict

class Solution:
    def canFinish(
        self, 
        numCourses: int, 
        prerequisites: List[List[int]]
    ) -> bool:
        if not prerequisites:
            return True

        adj = defaultdict(list)
        for src, dst in prerequisites:
            adj[src].append(dst)

        visit, path = set(), set()
        ans = []
        
        def dfs(node: int) -> bool:
            if node in visit:
                return False

            if node in path:
                return True

            path.add(node)

            for dst in adj[node]:
                if dfs(dst): return True


            path.remove(node)
            visit.add(node)
            ans.append(node)

        for i in range(numCourses):
            if dfs(i):
                return False

        return True