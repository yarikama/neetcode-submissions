# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_min_node(
        self,
        root: TreeNode,
    ) -> int:
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(
        self, 
        root: Optional[TreeNode], 
        key: int,
    ) -> Optional[TreeNode]:
        if root is None:
            return

        # Recursive
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = self.get_min_node(root)
                root.val = min_node.val
                self.deleteNode(root.left, min_node.val)

        return root



        





