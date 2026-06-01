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
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        curSum = max(node.val + left + right, node.val)
        self.maxSum = max(self.maxSum, curSum)
        
        return max(left + node.val, right + node.val, node.val, 0)


#            5
#       4        8
#     11  N   13   4
#    7  2    N  N N 1      