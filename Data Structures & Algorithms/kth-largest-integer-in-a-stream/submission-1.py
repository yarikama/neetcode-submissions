from typing import Optional

class Heap:
    def __init__(self):
        self.heap = [0]

    def __len__(self) -> int:
        return len(self.heap)

    def pop(self) -> Optional[int]:
        if len(self.heap) == 1:
            return None

        if len(self.heap) == 2:
            return self.heap.pop() 

        result = self.heap[1]
        self.heap[1] = self.heap.pop()

        # start with the root
        i = 1
        # check whether it is a leaf node
        while(len(self.heap) > 2*i):
            # check right
            if (
                len(self.heap) > 2*i+1
                and self.heap[i] > self.heap[2*i+1]
                and self.heap[2*i] > self.heap[2*i+1]
            ):
                tmp = self.heap[2*i+1]
                self.heap[2*i+1] = self.heap[i]
                self.heap[i] = tmp
                # next iteration
                i = 2*i+1
            # check left
            elif (
                self.heap[i] > self.heap[2*i]
            ):
                tmp = self.heap[2*i]
                self.heap[2*i] = self.heap[i]
                self.heap[i] = tmp
                # next iteration
                i = 2*i
            # break if it is leaf node
            else:
                break

        return result

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap)-1

        while(
            i > 1
            and self.heap[i] < self.heap[i//2]
        ):
            tmp = self.heap[i]
            self.heap[i] = self.heap[i//2]
            self.heap[i//2] = tmp
            i == i//2
        


class KthLargest:

    def __init__(
        self, 
        k: int, 
        nums: List[int],
    ):
        self.k = k
        self.nums = nums
        self.min_heap = Heap()

        for i in self.nums:
            self.add(i)
        
    def add(
        self, 
        val: int,
    ) -> Optional[int]:
        self.min_heap.push(val)
        if self.k < len(self.min_heap):
            return self.min_heap.pop()
