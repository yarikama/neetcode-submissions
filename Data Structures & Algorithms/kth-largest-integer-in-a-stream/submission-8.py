from heapq import heapify, heapreplace, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k

        if len(nums) < k:
            self.min_heap = nums
            heapify(nums)
        else:
            self.min_heap = []
            for num in nums:
                self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapreplace(self.min_heap, val)
        return self.min_heap[0]
            

