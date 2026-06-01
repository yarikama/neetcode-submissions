from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for from_i, to_i in tickets:
            heapq.heappush(adj[from_i], to_i)

        res = []
        def dfs(src: str) -> None:
            while adj[src]:
                dst = heapq.heappop(adj[src])
                dfs(dst)
            res.append(src)

        dfs('JFK')
        return res[::-1]