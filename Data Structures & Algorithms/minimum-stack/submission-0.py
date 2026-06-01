class MinStack:

    def __init__(self):
        self.arr = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
            return

        if self.min_stack[-1] < val:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.arr.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
