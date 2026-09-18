# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0

        if root is None:
            return self.res

        self.order = 0

        def helper(node: TreeNode) -> None:
            if node.left:
                helper(node.left)

            self.order += 1

            if self.order == k:
                self.res = node.val

            if node.right:
                helper(node.right)

        helper(root)

        return self.res