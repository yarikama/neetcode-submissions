from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)

        def dfs(root: int, visited: Set[int] = set()) -> int:
            visited.add(root)
            res = 0
            for chil in adj[root]:
                if chil not in visited:
                    chil_res = dfs(chil, visited)
                    res = max(res, chil_res)
            return 1 + res


        min_height = float("inf")
        res = []
        for root in range(n):
            curr_height = dfs(root, set())
            if curr_height < min_height:
                res = [root]
                min_height = curr_height
            elif curr_height == min_height:
                res.append(root)

        return res
