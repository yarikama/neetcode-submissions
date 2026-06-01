from typing import Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.get_depth_and_max_length(root)[0]

    def get_depth_and_max_length(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        max_length, depth = 0, 0
        
        if not root or (not root.left and not root.right):
            return max_length, depth

        left_max_length, left_depth = self.get_depth_and_max_length(root.left)
        right_max_length, right_depth = self.get_depth_and_max_length(root.right)


        if root.right and root.left:
            depth = max(left_depth+1, right_depth+1)
            max_length = max(left_depth+1 + right_depth+1, depth)
        elif root.left:
            depth = left_depth+1
            max_length = max(left_max_length, depth)
        else:
            depth = right_depth+1
            max_length = max(right_max_length, depth)

        return max_length, depth
        