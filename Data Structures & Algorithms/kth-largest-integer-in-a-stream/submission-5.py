from heapq import heapify_max, heappush_max, heappop, nlargest

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify_max(nums)

    def add(self, val: int) -> int:
        heappush_max(self.heap, val)
        return nlargest(self.k, self.heap)[-1]
