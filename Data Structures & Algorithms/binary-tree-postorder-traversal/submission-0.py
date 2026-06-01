# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = righ

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)]
        result = []

        while stack:
            node, visited = stack.pop()
            
            if not node:
                continue

            if visited:
                result.append(node.val)
                continue

            stack.append((node, True))
            stack.append((node.left, False))
            stack.append((node.right, False))
            
        return result