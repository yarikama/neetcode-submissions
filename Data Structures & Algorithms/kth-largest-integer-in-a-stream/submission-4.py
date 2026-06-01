from typing import Optional

class Heap:
    def __init__(self):
        self._heap = [0]

    def __len__(self) -> int:
       # THIS IS IMPORTANT
       return len(self._heap)-1

    @property
    def top(self) -> int:
        if len(self._heap) == 1:
            return 0
        return self._heap[1]

    def pop(self) -> Optional[int]:
        if len(self._heap) == 1:
            return None

        if len(self._heap) == 2:
            return self._heap.pop() 

        result = self._heap[1]
        self._heap[1] = self._heap.pop()

        # start with the root
        i = 1
        # check whether it is a leaf node
        while(len(self._heap) > 2*i):
            # check right
            if (
                len(self._heap) > 2*i+1
                and self._heap[i] > self._heap[2*i+1]
                and self._heap[2*i] > self._heap[2*i+1]
            ):
                tmp = self._heap[2*i+1]
                self._heap[2*i+1] = self._heap[i]
                self._heap[i] = tmp
                # next iteration
                i = 2*i+1
            # check left
            elif (
                self._heap[i] > self._heap[2*i]
            ):
                tmp = self._heap[2*i]
                self._heap[2*i] = self._heap[i]
                self._heap[i] = tmp
                # next iteration
                i = 2*i
            # break if it is leaf node
            else:
                break

        return result

    def push(self, val: int) -> None:
        self._heap.append(val)
        i = len(self._heap)-1

        while(
            i > 1
            and self._heap[i] < self._heap[i//2]
        ):
            tmp = self._heap[i]
            self._heap[i] = self._heap[i//2]
            self._heap[i//2] = tmp
            i = i//2
        


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
        if self.k > len(self.min_heap) or val >= self.min_heap.top:
            self.min_heap.push(val)
        if self.k < len(self.min_heap):
            # NOT TO RETURN THE NEW ONE
            self.min_heap.pop()
        #RETURN THIS ONE
        return self.min_heap.top