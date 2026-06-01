from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        # DS
        queue = deque()
        old_new_map = {}

        # Init
        node_copy = Node(node.val)
        queue.append(node_copy)
        old_new_map[node] = node_copy 

        # BFS
        while queue:
            cur = queue.popleft()
            
            for neighbor in cur.neighbors:
                # Base Case
                if neighbor not in old_new_map:
                    new_node = Node(neighbor.val)
                    old_new_map[neighbor] = new_node
                    queue.append(new_node)

                old_new_map[neighbor].neighbors.append(cur)

        return node_copy

