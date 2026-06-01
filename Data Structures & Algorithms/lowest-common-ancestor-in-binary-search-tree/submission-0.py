# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(
        self, 
        root: TreeNode, 
        p: TreeNode, 
        q: TreeNode
    ) -> TreeNode:

        def dfs(node: TreeNode) -> None | TreeNode:
            if not node: return

            s = set()

            left = dfs(node.left) 
            right = dfs(node.right)

            if isinstance(left, TreeNode): return left
            if isinstance(right, TreeNode): return right

            s.add(node.val)
            if left: s.update(left)
            if right: s.update(right)

            if p.val in s and q.val in s:
                return node

            return s
            

        return dfs(root)



        