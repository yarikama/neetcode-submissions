# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
cacheTrue = defaultdict(int)
cacheFalse = defaultdict(int)

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.helper(root, True), self.helper(root, False))

    def helper(self, root: Optional[TreeNode], isChoosed: bool) -> int:
        if not root:
            return 0

        if isChoosed:
            if root in cacheTrue:
                return cacheTrue[root]
            res = root.val + self.helper(root.left, False) + self.helper(root.right, False)
            cacheTrue[root] = res
            return res

        if root in cacheFalse:
            return cacheFalse[root]

        res = max(
            self.helper(root.left, True) + self.helper(root.right, True),
            self.helper(root.left, True) + self.helper(root.right, False),
            self.helper(root.left, False) + self.helper(root.right, True),
            self.helper(root.left, False) + self.helper(root.right, False)
        )
        cacheFalse[root] = res
        return res
