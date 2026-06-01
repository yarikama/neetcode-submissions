# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def dfs(node: TreeNode) -> bool:
            if not node.left and not node.right:
                return True
            if not node.left:
                return node.val < node.right.val and dfs(node.right)
            elif not node.right:
                return node.val > node.left.val and dfs(node.left)
            else:
                return node.left.val < node.val < node.right.val and dfs(node.right) and dfs(node.left)

        return dfs(root) 



        
        