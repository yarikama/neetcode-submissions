# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def getHeight(node: Optional[TreeNode]) -> Tuple[bool | int]:
            if not node:
                return True, 0

            is_left_balanced, left_height = getHeight(node.left)
            is_right_balanced, right_height = getHeight(node.right)

            if not is_left_balanced or not is_right_balanced:
                return False, 0

            if abs(left_height - right_height) > 1:
                return False, 0

            return True, max(left_height, right_height) + 1

        return getHeight(root)[0]