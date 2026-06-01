# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node: TreeNode | None, largest: int) -> int:
            add_on = 0
            if largest < node.val:
                largest = node.val
                add_on += 1

            if node.left:
                add_on += dfs(node.left, largest)
            if node.right:
                add_on += dfs(node.left, largest)

            return add_on

        return dfs(root, float('-inf'))
            

        