class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False

        def dfs(idx: int) -> int:
            if idx >= len(nums)-1:
                return idx

            max_step = nums[idx] # 5
            result = max_step + idx # 5

            for i in range(idx+1, idx+max_step+1):
                if i >= len(nums)-1:
                    return i
                for j in range(1, nums[i]+1):
                    result = max(dfs(nums[j] + j), result)

            return result                

        print(dfs(0))

        return dfs(0) >= len(nums) - 1