class Node:
    def __init__(
        self, 
        value: int, 
        next: Optional["Node"] = None, 
        prev: Optional["Node"] = None,
    ) -> "Node":
        self.value = value
        self.next = next
        self.prev = prev

class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1, prev=self.head)
        self.head.next = self.tail
        print(self)

    def __str__(self) -> str:
        i = 0
        string = ''
        current_node = self.head
        while(current_node):
            string += f"index: {i}, value: {current_node.value}\n"
            current_node = current_node.next
            i += 1
        return string

    def isEmpty(self) -> bool:
        return (
            self.head.next is self.tail 
            and self.tail.prev is self.head
        ) 

    def append(self, value: int) -> None:
        previous_node = self.tail.prev
        self.tail.prev = new_node = Node(
            value=value,
            next=self.tail,
            prev=previous_node,
        )
        previous_node.next = new_node

    def appendleft(self, value: int) -> None:
        next_node = self.head.next
        self.head.next = new_node = Node(
            value=value,
            next=next_node,
            prev=self.head,
        )
        next_node.prev = new_node

    def pop(self) -> int:
        value = self.tail.prev.value
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        return value

    def popleft(self) -> int:
        value = self.head.next.value
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return value
        
