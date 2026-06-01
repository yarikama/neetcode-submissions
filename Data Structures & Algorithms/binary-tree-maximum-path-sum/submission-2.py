# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val
        self.dfs(root)
        return self.maxSum

    def dfs(self, node: TreeNode) -> int:
        if not node: return 0

        left = max(self.dfs(node.left), 0)
        right = max(self.dfs(node.right), 0)
        curSum = max(node.val + left + right, node.val)
        self.maxSum = max(self.maxSum, curSum)

        return curSum


        
        