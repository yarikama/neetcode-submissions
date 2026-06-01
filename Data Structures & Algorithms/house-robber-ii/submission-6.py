class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)


        ans = deque([[nums[-3] + nums[-1], True], [nums[-2], False], [nums[-1], True]])
        for i in range(len(nums)-4, -1, -1):
            num, useLast = ans.pop()
            if ans[-1][0] > num:
                ans.appendleft([nums[i] + ans[-1][0], ans[-1][1]])
            elif ans[-1][0] < num:
                ans.appendleft([nums[i] + num, useLast])
            else:
                if useLast:
                    ans.appendleft([nums[i] + ans[-1][0], ans[-1][1]])

        print(ans)

        if ans[0][1]:
            ans[0][0] -= nums[-1] 

        print(ans)
        
        
        return max(val for val, _ in ans)