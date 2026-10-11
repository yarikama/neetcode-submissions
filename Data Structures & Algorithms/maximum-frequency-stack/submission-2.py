from collections import defaultdict
from heapq import heappush, heappop

class FreqStack:

    def __init__(self):
        self.counter = defaultdict(int)
        self.heap = []
        self.rank = 0

    def push(self, val: int) -> None:
        self.counter[val] += 1
        heappush(self.heap, [-1*self.counter[val], -1*len(self.heap), val])

    def pop(self) -> int:
        _, _, val = heappop(self.heap)
        self.counter[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()