# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _get_min_value(
        self,
        root: TreeNode,
    ) -> int:
        current_node = root
        while(current_node and current_node.left):
            current_node = current_node.left
        return current_node.val

    def _delete(
        self,
        node: TreeNode,
    ) -> Optional[TreeNode]:
        if node.left is None:
            return node.right
        
        if node.right is None:
            return node.left

        min_value = self._get_min_value(node.right)
        node.val = min_value
        node.right = self.deleteNode(
            root=node.right,
            key=min_value,
        )
        return node


    def deleteNode(
        self, 
        root: Optional[TreeNode], 
        key: int,
    ) -> Optional[TreeNode]:
        # Base Condition
        if root is None:
            return

        # Recursive
        if key > root.val:
            root.right = self.deleteNode(
                root=root.right,
                key=key,
            )
        elif key < root.val:
            root.left = self.deleteNode(
                root=root.left,
                key=key
            )
        else:
            return self._delete(node=root)

        return root



        





