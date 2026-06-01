class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for i in range(i, n+1):
            adj[i] = list()


        for u, v, time in times:
            adj[u].append((time, v))

        
        sp, pq = {}, [(0, k)] # time, node

        while pq:
            time, smallest_node = heappop(pq)

            if smallest_node in sp:
                continue

            for new_time, neighbor in adj[smallest_node]:
                heappush(pq, (time+new_time), neighbor)

            
        res = sp[k]

        for i in range(1, n+1):
           
            if i not in sp:
                return -1

            res = max(res, sp[i])

        return res