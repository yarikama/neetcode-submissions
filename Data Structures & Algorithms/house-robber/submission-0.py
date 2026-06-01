from collections import deque

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        ans = deque([nums[-3] + nums[-1], nums[-2], nums[-1]])
        for i in range(len(nums)-4, -1, -1):
            tmp = ans.pop()
            ans.appendleft(nums[i] + max(ans[-1], tmp))

        return max(ans)
        



# 2 9 8 3 6
# 3 6
#   14
