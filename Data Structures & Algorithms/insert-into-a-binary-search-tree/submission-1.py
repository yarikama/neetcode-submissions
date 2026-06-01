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
        if root is None:
            return TreeNode(val=val)

        if val > root.val:
            root.right = self.insertIntoBST(
                root=root.right, 
                val=val,
            )
        elif val < root.val:
            root.left = self.insertIntoBST(
                root=root.left,
                val=val,
            )

        return root

        