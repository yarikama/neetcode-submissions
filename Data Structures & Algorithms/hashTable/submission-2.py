from typing import Optional
class Node:
    def __init__(
        self, 
        key: int, 
        value: int, 
        next: Optional['Node'] = None,
    ):
        self.key = key
        self.value = value
        self.next = next or None

class HashTable:
    REHASH_RATIO = 0.5

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.bucket = [None] * self.capacity

    def hash_function(self, key: int):
        return key % self.capacity
        
    def insert(self, key: int, value: int) -> None:
        hash_key = self.hash_function[key]
        node = self.bucket[hash_key]

        if node is None:
            self.bucket[hash_key] = Node(key, value)
            return 

        prev = None
        while node:
            if node.key == key:
                node.value = value
                return

            prev = node
            node = node.next 

        prev.next = Node(key, value)
        self.size += 1

        if self.size / self.capacity >= REHASH_RATIO:
            self.resize()

    def get(self, key: int) -> int:
        hash_key = self.hash_function[key]
        node = self.bucket[hash_key]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> bool:
        hash_key = self.hash_function(key)
        prev, node = None, self.bucket[hash_key]
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.bucket[hash_key] = node.next
                self.size -= 1
                return True
            prev, node = node, node.next
        return False


    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_bucket = [None] * new_capacity

        for node in self.bucket:
            while node:
                new_hash_key = node.key % new_capacity

                if new_bucket[new_hash_key] is None:
                    new_bucket[new_hash_key] = Node(node.key, node.value)

                else:
                    new_head = new_bucket[new_hash_key]
                    while new_head.next:
                        new_head = new_head.next
                    new_head.next = Node(node.key, node.value)

                node = node.next

        self.capacity = new_capacity
        self.table = new_table

