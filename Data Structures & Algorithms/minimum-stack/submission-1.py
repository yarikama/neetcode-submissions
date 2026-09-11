class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = [float("inf")]
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if val <= self.mins[-1]:
            self.mins.append(val)
            return

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]

        
