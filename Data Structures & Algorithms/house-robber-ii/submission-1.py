class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        ans = deque([nums[-3], nums[-2], nums[-1]])
        for i in range(len(nums)-4, -1, -1):
            tmp = ans.pop()
            ans.appendleft(nums[i] + max(ans[-1], tmp))

        return max(ans)