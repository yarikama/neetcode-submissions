# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left_height = self.getDepth(root.left)
        right_height = self.getDepth(root.right)

        if abs(left_height-right_height) > 1:
            return False
        return True

    def getDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.getDepth(root.left), self.getDepth(root.right))+1
        