from typing import Optional

class ListNode:
    def __init__(
        self, 
        value: Optional[int] = None, 
        next: Optional["ListNode"] = None
    ) -> "ListNode":
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self) -> "LinkedList":
        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None

    def _is_empty(self) -> bool:
        return self.head is None or self.tail is None

    def get(self, index: int) -> int:
        if self._is_empty():
            return -1

        current_node = self.head
        for i in range(index):
            current_node = current_node.next
            if current_node is None:
                return -1

        return current_node.value

    def insertHead(self, val: int) -> None:
        self.head = ListNode(
            value = val, 
            next = self.head
        )

        if self._is_empty():
            self.tail = self.head

    def insertTail(self, val: int) -> None:
        if self._is_empty():
            self.head = self.tail = ListNode(value = val)
            return
    
        self.tail.next = ListNode(value = val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        if self._is_empty():
            return False

        previous_node: Optional[ListNode] = None
        current_node: Optional[ListNode] = self.head
        for i in range(index):
            previous_node = current_node
            if previous_node.next is None:
                return False
            current_node = previous_node.next

        if current_node is self.tail:
            return True

        previous_node.next = current_node.next
        return True 

    def getValues(self) -> List[int]:
        all_values: List[int] = []
        current_node = self.head
        while current_node:
            all_values.append(current_node.value)
            current_node = current_node.next

        return all_values

