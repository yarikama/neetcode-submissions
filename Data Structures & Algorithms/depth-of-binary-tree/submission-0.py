# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)

    def getDepth(self, root: Optional[TreeNode], depth: int = 0) -> int:
        if not root:
            return depth

        return max(self.getDepth(root.left, depth+1), self.getDepth(root.right, depth+1))