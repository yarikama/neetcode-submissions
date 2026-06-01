from collections import deque
from typing import Optional

class Node:
    def __init__(
        self,
        key: int,
        val: int,
        prev: Optional["Node"] = None,
        next: Optional["Node"] = None, 
    ) -> 'Node':
        self.key = key
        self.val = val
        self.prev = prev or None
        self.next = next or None

    def __repr__(self):
        string = "Val: " + str(val)
        if prev:
            string = "Prev: " + str(prev.val) + ", " + string
        if next:
            string = string + " Next: " + str(next.val)
        return string
        
class DoubledLinkedList:
    def __init__(
        self,
        head: Node | None = None,
        tail: Node | None = None,
    ) -> "DoubledLinkedList": 
        self.head = head or None
        self.tail = tail or None

    def append(self, node: Node) -> None:
        if not self.head and self.tail:
            self.head = self.tail = node
            return

        print(self.head)
        print(self.tail)
        self.tail.next = node
        node.prev = self.tail
        self.tail = self.tail.next

    def get_least_recent_used_node(self) -> Node:
        least_used_node = self.head
        self.head = self.head.next
        self.head.prev = None
        least_used_node.next = None
        return least_used_node


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._hash_map = {}
        self._double_linked_list = DoubledLinkedList()
        self._current_size = 0

    def get(self, key: int) -> int:
        if key not in self._hash_map:
            return -1

        node = self._hash_map[key]
        prev = node.prev
        next = node.next
        node.prev = None
        node.next = None

        if prev:
            prev.next = next
        if next:
            next.prev = prev

        self._double_linked_list.append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        self._hash_map[key] = node
        self._double_linked_list.append(node)
        self._current_size += 1

        # evict
        if self._current_size > self._capacity:
            evicted_node = _double_linked_list.get_least_recent_used_node()
            self._hash_map.pop[evicted_node.key]

        
