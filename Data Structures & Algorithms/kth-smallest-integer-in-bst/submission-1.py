# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0

        if root is None:
            return res

        order = 0

        def helper(node: TreeNode) -> None:
            if node.left:
                helper(node.left)

            nonlocal order 
            order += 1

            if order == k:
                nonlocal res
                res = node.val

            if node.right:
                helper(node.right)

        helper(root)

        return res