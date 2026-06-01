from heapq import *

# nums=[5,9,3,2,1,0,2,3,3,1,0,0]
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False

        def dfs(idx: int) -> int:
            if idx >= len(nums)-1:
                return idx

            max_step = nums[idx] # 5
            result = max_step + idx # 5

            for i in range(1, max_step+1):
                if idx + i >= len(nums)-1:
                    return idx + i
                # result = max(result, dfs(idx + nums[idx+i] + i))
                r = dfs(idx + nums[idx+i] + i)
                print(r)
                result = max(r, result)

            return result                

        print(dfs(0))

        return dfs(0) >= len(nums) - 1