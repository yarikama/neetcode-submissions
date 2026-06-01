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
        # Edge Case
        if not node:
            return

        # DS
        queue = deque()
        old_new_map = {}

        # Init
        node_copy = Node(node.val)
        queue.append(node) # queue 放原本的
        old_new_map[node] = node_copy 

        # BFS
        while queue:
            cur = queue.popleft()
            # Explore
            for neighbor in cur.neighbors:
                # Base Case
                if neighbor not in old_new_map:
                    new_node = Node(neighbor.val)
                    old_new_map[neighbor] = new_node
                    queue.append(neighbor)
                
                old_new_map[cur].neighbors.append(old_new_map[neighbor])

        return node_copy

