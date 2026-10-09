class Node:
    def __init__(self, L: int, R: int, left_node: "Node" | None = None, right_node: "Node" | None = None):
        self.L = L
        self.R = R
        self.left_node = left_node
        self.right_node = right_node

    def isOverlap(self, L: int, R: int) -> bool:
        if self.L <= L < self.R or self.L < R <= self.R:
            return True
        
        if L <= self.L < R or L < self.R <= R:
            return True
        
        return False


class MyCalendar:
    
    def __init__(self):
        self.root = None

    def book(self, startTime: int, endTime: int) -> bool:
        if self.root is None:
            self.root = Node(startTime, endTime)
            return True

        curr = self.root
        while curr:
            if curr.isOverlap(startTime, endTime):
                return False

            if startTime >= curr.R:
                if curr.right_node is None:
                    curr.right_node = Node(startTime, endTime)
                    return True
                curr = curr.right_node
            else:
                if curr.left_node is None:
                    curr.left_node = Node(startTime, endTime)
                    return True
                curr = curr.left_node

        return True



        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)