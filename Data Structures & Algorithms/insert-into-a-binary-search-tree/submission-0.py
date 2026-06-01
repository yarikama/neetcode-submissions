# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(
        self, 
        root: Optional[TreeNode], 
        val: int
    ) -> Optional[TreeNode]:
        self._insert(
            node=root,
            val=val,
        )
        return root

    def _insert(
        self, 
        node: Optional[TreeNode], 
        val: int,
    ) -> Optional[TreeNode]:
        if node is None:
            return TreeNode(val=val)

        if val > node.val:
            node.right = self._insert(
                node=node.right, 
                val=val,
            )
        elif val < node.val:
            node.left = self._insert(
                node=node.left,
                val=val,
            )

        return node

        