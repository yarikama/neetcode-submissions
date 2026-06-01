from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(
        self, 
        root: Optional[TreeNode],
    ) -> List[List[int]]:
        output = []
        self.queue = deque()

        if root:
            self.queue.append(root)

        while self.queue:
            level = []
            for i in range(len(self.queue)):
                current_node = self.queue.popleft()
                level.append(current_node.val)
                if current_node.left:
                    self.queue.append(current_node.left)
                if current_node.right:
                    self.queue.append(current_node.right)
            output.append(level)

        return output

            



        