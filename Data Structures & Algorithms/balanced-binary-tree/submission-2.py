from typing import Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[0]

    def helper(self, root: Optional[TreeNode]) -> Tuple[bool, int]:
        if not root:
            return True, 0

        is_left_balanced, left_height = self.helper(root.left)
        if not is_left_balanced:
            return False, 0

        is_right_balanced, right_height = self.helper(root.right)
        if not is_right_balanced:
            return False, 0

        if abs(left_height - right_height) > 1:
            return False, 0

        return True, max(right_height, left_height) + 1
        