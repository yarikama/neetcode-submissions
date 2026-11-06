class MinHeap:
    def __init__(self):
        self.arr = [-1]
        
    def push(self, val: int) -> None:
        self.arr.append(val)
        i = len(self.arr) - 1
        while i > 1 and self.arr[i] < self.arr[i//2]:
            tmp = self.arr[i//2]
            self.arr[i//2] = self.arr[i]
            self.arr[i] = tmp
            i = i//2

    def _bubble_down(self, i: int) -> None: 
        while len(self.arr) > 2*i:
            if (
                len(self.arr) > 2*i+1
                and self.arr[2*i+1] < self.arr[i]
                and self.arr[2*i+1] < self.arr[2*i]
            ):
                tmp = self.arr[i]
                self.arr[i] = self.arr[2*i+1]
                self.arr[2*i+1] = tmp 
                i = 2*i+1
            elif self.arr[2*i] < self.arr[i]:
                tmp = self.arr[i]
                self.arr[i] = self.arr[2*i]
                self.arr[2*i] = tmp
                i = 2*i
            else:
                break

    def pop(self) -> int:
        if len(self.arr) == 1:
            return self.arr[0]

        if len(self.arr) == 2:
            return self.arr.pop()

        result = self.arr[1]
        self.arr[1] = self.arr.pop()
        self._bubble_down(1)
        return result

    def top(self) -> int:
        if len(self.arr) == 1:
            return self.arr[0]
        return self.arr[1]        

    def heapify(self, nums: List[int]) -> None:
        self.arr = [-1] + nums
        youngest_parent = (len(self.arr)-1)//2
        for idx in range(youngest_parent, 0, -1):
            self._bubble_down(idx)
        












        
        