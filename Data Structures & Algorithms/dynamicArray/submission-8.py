class DynamicArray:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        self.size += 1
        if self.size > self.capacity:
            self.resize()
        self.array[self.size - 1] = n 

    def popback(self) -> int:
        self.size -= 1
        return self.array[self.size]

    def resize(self) -> None:
        self.array += [0] * self.capacity
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
