# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(
        self, root: Optional[TreeNode], key: int
    ) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = self.get_min_node(root.right)
                root.val = min_node.val
                root.right = self.deleteNode(root.right, min_node.val)

        return root

    def get_min_node(self, root: TreeNode) -> TreeNode:
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr