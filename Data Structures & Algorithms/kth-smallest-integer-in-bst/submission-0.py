# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(
        self, 
        root: Optional[TreeNode], 
        k: int
    ) -> int:
        self.k = k
        self.result = -1
        self._inorder_traversal(root)
        return self.result

    def _inorder_traversal(
        self,
        node: Optional[TreeNode],
    ) -> None:
        if node is None or self.k < 0:
            return

        self._inorder_traversal(
            node=node.left
        )

        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return
            
        self._inorder_traversal(
            node=node.right
        )
        