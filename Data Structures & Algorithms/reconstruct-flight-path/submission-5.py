from collections import defaultdict
import heapq

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 1. 建立鄰接串列，並使用 Min-Heap 確保我們總是先走字母順序小的
        adj = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)
            
        res = []
        
        def dfs(curr):
            # 2. 當這個機場還有票可以飛時
            while adj[curr]:
                # 每次取出字母順序最小的目標
                next_dest = heapq.heappop(adj[curr])
                dfs(next_dest)
            # 3. 如果沒有路可以走了，就加入路徑（這會是逆序加入）
            res.append(curr)
            
        dfs("JFK")
        # 4. 最後將結果翻轉回來
        return res[::-1]