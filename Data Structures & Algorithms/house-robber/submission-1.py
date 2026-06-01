from collections import deque

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cur, prev = 0, 0
        for num in nums:
            tmp = cur
            cur = max(
                cur, # 不選
                prev + num, # 前一個 + 現在的
            )
            prev = tmp

        return cur



# 2 9 8 3 6
# 3 6
#   14
