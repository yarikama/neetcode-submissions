"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        head_cpy = Node(head.val) 
        hash = {head: head_cpy}

        cur = head
        while cur:
            next = cur.next
            if next:
                if next not in hash:
                    hash[next] = Node(next.val)
                next_cpy = hash[next]
                hash[cur].next = next_cpy

            random = cur.random
            if random:
                if random not in hash:
                    hash[random] = Node(random.val)
                random_cpy = hash[random]
                hash[cur].random = random_cpy 

            cur = next

        return hash[head]
            
        