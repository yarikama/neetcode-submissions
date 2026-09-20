"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import defaultdict

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cache = defaultdict()

        def dfs(node: Optional['Node']) -> Optional[Node]:
            if node is None: 
                return node

            if node in cache: 
                return cache[node]

            new_node = Node(node.val)
            cache[node] = new_node

            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))

            return new_node

        return dfs(node)

        