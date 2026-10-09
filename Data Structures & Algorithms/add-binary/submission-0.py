from collections import deque

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a

        b = "0" * (len(a) - len(b)) + b

        carry = "0"
        queue = deque()
        for i in range(len(b)):
            if a[-1-i] == "1" and b[-1-i] == "1":
                queue.appendleft(carry)
                carry = "1"
            elif a[-1-i] == "0" and b[-1-i] == "0":
                queue.appendleft(carry)
                carry = "0"
            elif carry == "1":
                queue.appendleft("0")
            else:
                queue.appendleft("1")
        
        return carry + "".join(queue) if carry == "1" else "".join(queue)


        