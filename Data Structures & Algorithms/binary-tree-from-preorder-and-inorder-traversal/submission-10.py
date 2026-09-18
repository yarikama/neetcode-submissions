# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        hashmap = {}

        for idx, val in enumerate(inorder):
            hashmap[val] = idx

        def helper(s_pre, e_pre, s_in, e_in):
            if s_pre > e_pre:
                return None

            node = TreeNode(preorder[s_pre])

            idx = hashmap[preorder[s_pre]]
            left_size = idx - s_in

            node.left = helper(
                s_pre + 1, s_pre + left_size, 
                s_in, idx - 1
            )
            node.right = helper(
                s_pre + left_size + 1, e_pre,
                idx + 1, e_in 
            )

            return node

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
