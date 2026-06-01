from heapq import heappop, heappush, nlargest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1

        pq = []
        for num, freq in cnt.items():
            heappush(pq, (freq, num))
        
        return [num for freq, num in nlargest(k, pq)]
        