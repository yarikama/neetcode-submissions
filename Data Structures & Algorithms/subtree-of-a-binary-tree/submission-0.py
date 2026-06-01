# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if not root and subRoot:
            print("no root")
            return False

        if root and not subRoot:
            print("no subRoot")
            return False

        if root.val != subRoot.val:
            print(f"root = {root.val} != {subRoot.val} = subRoot")
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 
        else:
            print(f"root = {root.val} == {subRoot.val} = subRoot")
            return self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)

        
        