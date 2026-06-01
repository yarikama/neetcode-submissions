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
            # 剪枝
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # 剪枝
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                # 剪枝
                return root.right
            elif not root.right:
                # 剪枝
                return root.left
            else:
                min_node = self.get_min_node(root.right)
                root.val = min_node.val
                # 剪枝
                root.right = self.deleteNode(root.right, min_node.val)

        return root



        





