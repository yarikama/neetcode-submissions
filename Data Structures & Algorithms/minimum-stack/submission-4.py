class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.min = val
            self.stack.append(0)
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def top(self) -> int:
        return self.min if self.stack[-1] < 0 else self.min + self.stack[-1]

    def pop(self) -> None:
        if not self.stack:
            return

        val = self.stack.pop()
        if val < 0:
            self.min = self.min - val

    def getMin(self) -> int:
        return self.min

        
