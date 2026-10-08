class Node:
    def __init__(
        self, 
        total: int,
        L: int,
        R: int,
    ):
        self.sum = total
        self.left, self.right = None, None
        self.L, self.R = L, R


class SegmentTree:
    
    def __init__(self, nums: List[int]):
        L, R = 0, len(nums)-1
        self.root = self.build(nums, L, R)

    def build(self, nums: List[int], L: int, R: int) -> None:
        if L == R: return Node(nums[R], L, R)

        M = (L + R) >> 1
        root = Node(0, L, R)
        root.left = self.build(nums, L, M)
        root.right = self.build(nums, M+1, R)
        root.sum = root.left.sum + root.right.sum
        return root
    
    def update(self, index: int, val: int) -> None:

        def helper(root: Node, index: int, val: int) -> None:
            if root.L == root.R: 
                root.sum = val
                return

            M = (root.L + root.R) >> 1
            if index > M:
                helper(root.right, index, val)
            else:
                helper(root.left, index, val)

            root.sum = root.left.sum + root.right.sum

        return helper(self.root, index, val)

    
    def query(self, L: int, R: int) -> int:

        def helper(root: Node, L: int, R: int) -> int:
            if R >= root.R and L <= root.L:
                return root.sum

            if L > root.R or R < root.L:
                return 0

            return helper(root.left, L, R) + helper(root.right, L, R)

        return helper(self.root, L, R)



    

