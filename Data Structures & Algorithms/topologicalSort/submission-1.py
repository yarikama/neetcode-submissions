class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj, ans, visit, path = defaultdict(list), [], set(), set()

        for src, dst in edges:
            adj[src].append(dst)

        def dfs(src: int) -> None:
            if src in visit:
                return False
            if src in path:
                return True

            path.add(src)

            for dst in adj[src]:
                if dfs(dst):
                    return True
                
            path.remove(src)
            visit.add(src)
            ans.append(src)

        for i in range(n):
            if dfs(i):
                return []

        return ans[::-1]
