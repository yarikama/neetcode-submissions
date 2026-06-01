from typing import Optional

class Node:
    def __init__(
        self,
        value: int,
        next: Optional['Node'] = None,
        prev: Optional['Node'] = None,
    ) -> 'Node':
        self.value = value
        self.next = next
        self.prev = prev


class Deque:
    
    def __init__(self):
        self.head = self.tail = None

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def _init_first_node(value: int) -> bool:
        if not self.isEmpty():
            return False

        self.head = self.tail = Node(value)
        return True

    def append(self, value: int) -> None:
        if self._init_first_node(value):
            return

        new_node = Node(
            value=value,
            prev=self.tail,
        )
        self.tail.next = new_node
        self.tail = self.tail.next

    def appendleft(self, value: int) -> None:
        if self._init_first_node(value):
            return

        new_node = Node(
            value=value,
            next=self.head,
        )        
        self.head.prev = new_node
        self.head = self.head.prev

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        value = self.tail.value
        previous_node = self.tail.prev
        if previous_node is not None:
            previous_node.next = None 
        self.tail = self.tail.prev
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        value = self.head.value
        next_node = self.head.next
        if next_node is not None:
            next_node.prev = None 
        self.head = self.head.next
        return value
