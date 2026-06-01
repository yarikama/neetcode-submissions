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
        
        path = set()
        ans = defaultdict(set)
        def dfs(node: int) -> bool | list[int]:
            if node in ans: return ans[node]
            if node in path: return True

            path.add(node)
            for dst in adj[node]:
                result = dfs(dst)
                if result is True:
                    return True
                else:
                    ans[node].add(dst)
                    ans[node] = ans[node].union(result)
            path.remove(node)

            return ans[node]

        for i in range(numCourses):
            if dfs(i) is True: 
                return [False for _ in range(numCourses)]

        print(ans)
        
        return [bool(dst in ans[src]) for src, dst in queries]

            