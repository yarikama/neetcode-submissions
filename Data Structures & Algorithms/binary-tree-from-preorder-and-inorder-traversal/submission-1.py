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
        self.preorder = preorder
        self.max_index = len(preorder) -1
        # Do bucket sort here for time complexity for O(1)
        # because the value might be negative
        self.radix_bucket = [0] * 2000
        for idx, value in enumerate(inorder):
            self.radix_bucket[value + 1000] = idx

        return self.connect_node(
            start_index=0,
            end_index=self.max_index,
        )

    
    def connect_node(
        self,
        start_index: int,
        end_index: int, 
        preorder_index: int = 0,
    ) -> Optional[TreeNode]:
        if start_index > end_index:
            return None

        if preorder_index > self.max_index:
            print(preorder_index)
            return None

        target_value = self.preorder[preorder_index]
        tree_node = TreeNode(val=target_value)


        if start_index == end_index:
            return tree_node


        # if start_index > end_index:
            # return None

        target_index = self.radix_bucket[target_value + 1000]

        #left connect
        tree_node.left = self.connect_node(
            start_index=start_index,
            end_index=target_index-1,
            preorder_index=preorder_index + 1, 
        )
        tree_node.right = self.connect_node(
            start_index=target_index+1,
            end_index=end_index,
            preorder_index=preorder_index + target_index - start_index + 1,
        )
        return tree_node





        

        
        
        