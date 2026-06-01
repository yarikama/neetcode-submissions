from typing import Set
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
        for after, before in prerequisites:
            adj[after].append(before)

        path = set()
        visited = set()

        def dfs(src: int) -> bool:
            if src in path:
                return False

            if src in visited:
                return True

            path.add(src)
            for dst in adj[src]:
                if not dfs(dst):
                    return False
            path.remove(src)
            visited.add(src)

            return True

        for src in range(numCourses):
            if not dfs(src):
                return False

        return True


        

