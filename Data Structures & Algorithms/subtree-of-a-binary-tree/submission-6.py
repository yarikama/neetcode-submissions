# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# IMPORTANT:
# DON'T PRINT ANYTHING!!!

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode], check_all: bool=False) -> bool:
        if not root and not subRoot:
            return True

        if not root and subRoot:
            return False

        if root and not subRoot:
            if check_all:
                return False
            else:
                return True

        # check descendent first -> or the complexity would be too high
        if not check_all and (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)):
            return True

        if root.val != subRoot.val:
            return False
        else:
            return self.isSubtree(root.left, subRoot.left, True) and self.isSubtree(root.right, subRoot.right, True)


        # if root.val != subRoot.val:
        #     if check_all:
        #         return False
        #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 
        # else:
        #     if (self.isSubtree(root.left, subRoot.left, True) and self.isSubtree(root.right, subRoot.right, True)):
        #         return True
        #     if self.isSubtree(root.left, subRoot) and not check_all:
        #         return True
        #     if self.isSubtree(root.right, subRoot) and not check_all:
        #         return True
        #     return False

        
        