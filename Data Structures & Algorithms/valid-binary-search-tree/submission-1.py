# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(
            node: TreeNode, upper_bound: int, lower_bound: int
        ) -> bool:
            if not node:
                return True
            if not (lower_bound < node.val < upper_bound):
                return False    
            if not node.left and not node.right:
                return True
            if not node.left:
                return node.val < node.right.val and dfs(node.right, upper_bound, node.val)
            elif not node.right:
                return node.val > node.left.val and dfs(node.left, node.val, lower_bound)
            else:
                return node.left.val < node.val < node.right.val and dfs(node.right, upper_bound, node.val) and dfs(node.left, node.val, lower_bound)

        return dfs(root) 



        
        