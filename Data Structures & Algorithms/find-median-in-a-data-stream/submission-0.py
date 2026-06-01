from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.small = [] # max_heap
        self.large = [] # min_heap
        
    def addNum(self, num: int) -> None:
        heappush(self.small, num * -1)

        if self.small and self.large:
            if self.small[0] * -1 > self.large[0]:
                val = heappop(self.small) * -1
                heappush(self.large, val)
            
        if len(self.small) > len(self.large) + 1:
            val = heappop(self.small) * -1
            heappush(self.large, val)

        if len(self.small) + 1 < len(self.large):
            val = heappop(self.large) * -1
            heappush(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0] * -1
        if len(self.small) < len(self.large):
            return self.large[0]
        return (self.small[0] * -1 + self.large[0]) / 2
        