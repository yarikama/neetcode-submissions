class Node:

    def __init__(
        self, 
        val: int, 
        prev: None | "Node" = None, 
        next: None | "Node" = None,
    ):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1, self.head)
        self.head.next = self.tail

    def getNode(self, index: int) -> 'Node' | None:
        i, curr = 0, self.head.next
        while curr and curr.next:
            if i == index:
                return curr
            curr = curr.next
            i += 1
        return curr

    def get(self, index: int) -> int:
        return self.getNode(index).val

    def addAtHead(self, val: int) -> None:
        if self.head.next is self.tail:
            node = Node(val, self.head, self.tail)
            self.head.next = node
            self.tail.prev = node
            return

        self.head.next = Node(val, self.head, self.head.next)
        self.head.next.next.prev = self.head.next

    def addAtTail(self, val: int) -> None:
        if self.head.next is self.tail:
            node = Node(val, self.head, self.tail)
            self.head.next = node
            self.tail.prev = node
            return

        self.tail.prev = Node(val, self.tail.prev, self.tail)
        self.tail.prev.prev.next = self.tail.prev

    def addAtIndex(self, index: int, val: int) -> None:
        prev, curr = self.head, self.head.next

        i = 0
        while curr:
            if i == index:
                node = Node(val, prev, curr)
                prev.next = node
                curr.prev = node
                return

            prev = curr
            curr = curr.next
            i += 1
        return
        

    def deleteAtIndex(self, index: int) -> None:
        prev, curr = self.head, self.head.next

        i = 0
        while curr:
            if i == index and curr is not self.tail:
                prev.next = curr.next
                curr.next.prev = prev
                return

            prev = curr
            curr = curr.next
            i += 1
        return     
        
    def printAll(self, func_name: str = "Start") -> None:
        curr = self.head
        print(func_name)
        while curr:
            print(curr.val, "-> ", end="")
            curr = curr.next
        print("")

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)