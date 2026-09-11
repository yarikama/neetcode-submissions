class Node:

    def __init__(self, val: int, next_node: Optional['Node'] = None) -> None:
        self.val = val
        self.next = next_node or None

    def __str__(self) -> str:
        return str(self.val)


class LinkedList:
    
    def __init__(self):
        # head remains dummy
        self.head = self.tail = Node(-1)
    
    def get(self, index: int) -> int:
        i, curr = 0, self.head
        while curr and i < index:
            curr = curr.next
            i += 1

        # run to target here, not the previous
        if curr and curr.next:
            return curr.next.val
        else:
            return -1

    def insertHead(self, val: int) -> None:
        # head remain dummy node
        node = Node(val, self.head.next)
        if self.head.next is None:
            self.tail = node
        self.head.next = node

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i, curr = 0, self.head
        while curr and i < index:
            curr = curr.next
            i += 1

        if curr and curr.next:
            if curr.next is self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        vals = []
        curr = self.head.next
        while curr:
            vals.append(curr.val)
            curr = curr.next

        return vals
        
