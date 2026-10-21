"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(L, R, T, B, Print = False) -> Node:
            root = Node()

            # Base
            if L+1 == R and T+1 == B:
                root.isLeaf = True
                root.val = True if grid[T][L] == 1 else False
                return root

            # Recursive
            horizontal_mid, vertical_mid = (L + R) // 2, (T + B) // 2
            topLeft =     helper(L, horizontal_mid, T, vertical_mid)
            topRight =    helper(horizontal_mid, R, T, vertical_mid)
            bottomLeft =  helper(L, horizontal_mid, vertical_mid, B)
            bottomRight = helper(horizontal_mid, R, vertical_mid, B)

            if (topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf) and \
                (topLeft.val is topRight.val is bottomLeft.val is bottomRight.val):
                root.val = topLeft.val
                root.isLeaf = True
                return root

            root.topLeft = topLeft
            root.topRight = topRight
            root.bottomLeft = bottomLeft
            root.bottomRight = bottomRight

            return root

        return helper(0, len(grid[0]), 0, len(grid), True)
