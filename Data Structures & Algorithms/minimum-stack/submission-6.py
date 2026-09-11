class MinStack:

    def __init__(self):
        self.min = float("inf")
        self.stack = []
        

    def push(self, val: int) -> None:
        # only record the diff in the stack
        if not self.stack:
            self.stack.append(0)
            self.min = val
            return

        diff = val - self.min
        self.stack.append(diff)

        # val is smaller than min, switch min
        if diff < 0:
            self.min = val



    def pop(self) -> None:
        val = self.stack.pop()

        # means we have to switch the min
        if val < 0:
            self.min = self.min - val # min - (min - last_min) = last_min 

    def top(self) -> int:
        return self.min if self.stack[-1] < 0 else self.min + self.stack[-1]

    def getMin(self) -> int:
        return self.min
