from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for src, dst in prerequisites:
            adj[src].append(dst)

        visit, path = set(), set()
        ans = []

        def dfs(node: int) -> bool:
            # Base Cases
            if node in visit: return False
            if node in path: return True

            # Post Order Traversal
            path.add(node) # Backtracking
            for dst in adj[node]:
                if dfs(dst): return True

            path.remove(node)
            # For duplicate
            visit.add(node)

            # Post Order Traversal
            ans.append(node)

        for i in range(numCourses):
            if dfs(i): return []

        return ans



                


            