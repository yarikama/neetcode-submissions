from typing import Set

class Solution:
    def canFinish(
        self, 
        numCourses: int, 
        prerequisites: List[List[int]]
    ) -> bool:
        if not prerequisites:
            return True

        graph = {}
        for src, dst in prerequisites:
            if src not in graph:
                graph[src] = []
            if dst not in graph:
                graph[dst] = []
            graph[src].append(dst)

        print(graph)


        def dfs(node: int, path: Set[int], graph: Dict[int, List[int]]) -> bool:
            # base case
            if node in path:
                return False

            if node not in graph:
                return True

            path.add(node)
            for n_node in graph[node]:
                if dfs(n_node, path, graph) is False:
                    return False

            path.remove(node)
            return True
        
        for i in range(numCourses):
            if dfs(i, set(), graph) is False:
                return False

        return True