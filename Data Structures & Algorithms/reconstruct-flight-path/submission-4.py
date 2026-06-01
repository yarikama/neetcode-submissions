from collections import defaultdict
from heapq import *

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        for src, dst in tickets:
            adj[src].append(dst)

        def dfs(
            src: str, ans: List[str], visited: Set[str],
        ) -> List[str]:
            if len(visited) == len(tickets):
                ans.append(src)
                return ans

            ans.append(src)
            for dst in adj[src]:
                if (src, dst) in visited:
                    continue

                visited.add((src, dst))

                result = dfs(dst, ans, visited)
                if result is not None:
                    return result

                visited.remove((src, dst))

            ans.pop()
            return

        return dfs('JFK', [], set()) or []

             

        


        