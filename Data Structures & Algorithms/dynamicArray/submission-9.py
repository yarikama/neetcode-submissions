class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [0] * self.capacity
        self.size = 0

    def __is_valid(self, i: int) -> bool:
        return i < self.size

    def get(self, i: int) -> int:
        return self.arr[i] if self.__is_valid(i) else -1

    def set(self, i: int, n: int) -> None:
        if self.__is_valid(i):
            self.arr[i] = n
        else:
            return


    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.size] 
 

    def resize(self) -> None:
        self.arr += [0] * self.capacity
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
