import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # to get a reverse stones
        for idx, val in enumerate(stones):
            stones[idx] = -val

        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -1 * abs(x - y))
            
        if stones:
            return -1 * stones[0]
        
        return 0