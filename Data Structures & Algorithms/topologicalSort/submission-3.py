class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        ans = []
        visit, path = set(), set()

        for src, dst in edges:
            adj[src].append(dst)

        def dfs(node: int) -> bool:
            # Base Case
            if node in visit:
                return False

            if node in path:
                return True

            path.add(node)

            for dst in adj[node]:
                if dfs(dst):
                    return True
            
            ans.append(node)
            visit.add(node)
            path.remove(node)

        for i in range(n):
            if dfs(i):
                return []
        
        return ans[::-1]