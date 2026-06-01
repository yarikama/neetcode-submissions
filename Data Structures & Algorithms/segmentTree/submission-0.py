from typing import List

class Node:

    def __init__(
        self,
        lim_l: int,
        lim_r: int,
        sum: int,
        left: 'Node' = None,  # 'Node' 的寫法是正確的前向引用 (forward reference)
        right: 'Node' = None,
    ) -> 'Node':

        # 錯誤 1：使用參數 lim_l 和 lim_r，而不是未定義的 L 和 R
        self.lim_l, self.lim_r = lim_l, lim_r
        self.sum = sum
        self.left, self.right = left, right


class SegmentTree:

    def __init__(self, nums: List[int]):
        # 處理空陣列的邊界情況
        if not nums:
            self.root = None
        else:
            self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums: List[int], L: int, R: int):
        if L == R:
            return Node(
                lim_l=L,
                lim_r=R,
                sum=nums[L],
            )

        # 錯誤 2：使用整數除法 //
        M = (L + R) // 2
        left = self.build(
            nums=nums,
            L=L,
            R=M,
        )
        right = self.build(
            nums=nums,
            L=M + 1,
            R=R,
        )
        return Node(
            lim_l=L,
            lim_r=R,
            sum=left.sum + right.sum,
            left=left,
            right=right,
        )

    def update(self, index: int, val: int) -> None:
        if self.root:
            self.update_helper(
                node=self.root,
                index=index,
                val=val
            )

    def update_helper(self, node: Node, index: int, val: int) -> None:
        if node.lim_l == node.lim_r:
            node.sum = val
            return

        # 錯誤 2：使用整數除法 //
        M = (node.lim_l + node.lim_r) // 2
        if M < index:
            self.update_helper(node.right, index, val)
        else:
            self.update_helper(node.left, index, val)
        node.sum = node.left.sum + node.right.sum

    def query(self, L: int, R: int) -> int:
        if not self.root:
            return 0  # 或者根據需求引發錯誤
        return self.query_helper(self.root, L, R)

    def query_helper(self, node: Node, L: int, R: int) -> int:
        # 節點範圍 [node.lim_l, node.lim_r]
        # 查詢範圍 [L, R]
        
        # 節點範圍完全等於查詢範圍
        if node.lim_l == L and node.lim_r == R:
            return node.sum

        # 錯誤 2：使用整數除法 //
        M = (node.lim_l + node.lim_r) // 2
        
        # 查詢範圍 [L, R] 完全在右子樹 [M+1, node.lim_r]
        if L > M:
            return self.query_helper(node.right, L, R)
        # 查詢範圍 [L, R] 完全在左子樹 [node.lim_l, M]
        elif R <= M:
            return self.query_helper(node.left, L, R)
        # 查詢範圍 [L, R] 跨越了左右子樹
        else:
            return self.query_helper(node.left, L, M) + self.query_helper(node.right, M + 1, R)