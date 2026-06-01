class DynamicArray:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.array = [0 * self.capacity]
        print("init", len(self.array))

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        self.size += 1
        if self.size > self.capacity:
            self.resize()
        print("size", self.size-1)
        print("capacity", self.capacity)
        print("length of array", len(self.array))
        self.array[self.size - 1] = n 

    def popback(self) -> int:
        last_element = self.array[self.size - 1]
        self.size -= 1
        return last_element

    def resize(self) -> None:
        print("before:", len(self.array))
        self.array += [0 * self.capacity]
        print("after:", len(self.array))

        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
