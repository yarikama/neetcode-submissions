from collections import deque
from math import log2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque()
        q.append(root)

        ans = []
        while q:
            isAllNone = True
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    ans.append('N')
                    q.append(node)
                    q.append(node)
                else:
                    ans.append(f'{node.val}')
                    q.append(node.left)
                    q.append(node.right)
                    isAllNone = False
            if isAllNone:
                print(ans)
                return ",".join(ans)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        q1 = data.split(',')
        for i in range(len(q1)):
            if q1[i] == 'N':
                q1[i] = None
            else:
                q1[i] = int(q1[i])
        if not q1[0]:
            return None

        root = TreeNode(q1[0])
        q2 = deque()
        q2.append((root, 0))
        while q2:
            node, idx = q2.popleft()
            left_idx, right_idx = 2 * idx + 1, 2 * idx + 2
            if q1[left_idx]:
                left = TreeNode(q1[left_idx])
                node.left = left
                q2.append((left, left_idx))
            if q1[right_idx]:
                right = TreeNode(q1[right_idx])
                node.right = right
                q2.append((right, right_idx))
            
        return root
        











