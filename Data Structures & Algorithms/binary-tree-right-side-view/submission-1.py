# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # self.queue = deque()

        # if root:
        #     self.queue.append(root)

        # right_side_nums = []

        # while self.queue:
        #     length_of_queue = len(self.queue)
        #     for i in range(length_of_queue):
        #         current_node = self.queue.popleft()
        #         if i == length_of_queue -1:
        #             right_side_nums.append(current_node.val)
        #         if current_node.left:
        #             self.queue.append(current_node.left)
        #         if current_node.right:
        #             self.queue.append(current_node.right)

        # return right_side_nums
        if not root:
            return []

        res = []
        curr = root
        while curr:
            res.append(curr.val)
            curr = curr.right
        return res









