import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify(stones)
        while len(stones) > 1:
            x = stones.pop()
            y = stones.pop()
            if x != y:
                stones.append(abs(x - y))
            
        return stones[0]