# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = righ

# in-order would iterate from the most left side to the most right side

class Solution:
    def inorderTraversal(
        self, 
        root: Optional[TreeNode]
    ) -> List[int]:
        self._result = []
        self._traversal(root)
        return self._result

    def _traversal(
        self,
        node: Optional[TreeNode]
    ) -> None:
        if node is None:
            return

        self._traversal(node.left)
        self._result.append(node.val)
        self._traversal(node.right)
        