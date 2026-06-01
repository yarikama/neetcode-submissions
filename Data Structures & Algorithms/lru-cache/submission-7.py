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
        
class DoubledLinkedList:
    def __init__(
        self,
        head: Node | None = None,
        tail: Node | None = None,
    ) -> "DoubledLinkedList": 
        self.head = head or Node(0, 0)
        self.tail = tail or Node(0, 0)

    def append(self, node: Node) -> None:
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node: Node) -> None:
        next = node.next
        prev = node.prev
        node.next = None
        node.prev = none
        next.prev = prev
        prev.next = next

    def pop_least_recent_node(self) -> Node:
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        node.next = None
        node.prev = None
        return node 

    def update(self, node: Node) -> None:
        self.remove(node)
        self.append(node)

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._hash_map = {}
        self._dll = DoubledLinkedList()
        self._current_size = 0

    def get(self, key: int) -> int:
        if key not in self._hash_map:
            return -1

        node = self._hash_map[key]
        self._dll.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self._hash_map:
            node = self._hash_map[key]
            node.val = value
            self._dll.update(node)
            return

        node = Node(key, value)
        self._hash_map[key] = node
        self._dll.append(node)
        self._current_size += 1

        # evict
        if self._current_size > self._capacity:
            evicted_node = self._dll.pop_least_recent_node()
            self._current_size -= 1
            self._hash_map.remove(evicted_node.key)

        
