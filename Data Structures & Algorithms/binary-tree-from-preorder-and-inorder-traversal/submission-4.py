# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(
        self, 
        preorder: List[int], 
        inorder: List[int],
    ) -> Optional[TreeNode]:
        inorder_indices = {value: idx for idx, value in enumerate(inorder)}
        pre_idx = 0
        def dfs(L: int, R: int) -> Optional[TreeNode]:
            if L > R:
                return None

            nonlocal pre_idx
            root_val = preorder[pre_idx]
            root_node = TreeNode(root_val)
            self.pre_idx += 1
            ino_idx = inorder_indices[root_val]
            root.left = dfs(L, ino_idx-1)
            root.right = dfs(ino_idx+1, R)
            return root
        return dfs(0, len(preorder)-1)

        # def connect_node(
        #     L: int,
        #     R: int, 
        #     preorder_index: int,
        # ) -> Optional[TreeNode]:
        #     if L > R:
        #         return None

        #     val = preorder[preorder_index]
        #     tree_node = TreeNode(val)

        #     if L == R:
        #         return tree_node

        #     inorder_index = inorder_indices[val]
        #     tree_node.left = connect_node(L, inorder_index-1, preorder_index+1)
        #     tree_node.right = connect_node(inorder_index+1, R, preorder_index + inorder_index - L + 1)
        #     return tree_node

        # return connect_node(0, len(preorder)-1, 0)





        

        
        
        