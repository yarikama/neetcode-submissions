from copy import deepcopy

class Solution:
    def subsets(
        self, 
        nums: List[int],
    ) -> List[List[int]]:
        result = [[]]
        if not nums:
            return result

        total_nums = len(nums)

        def dfs(index: int, subset: List[int]) -> None:
            if index == total_nums: return

            subset1 = subset.copy() + [nums[index]]
            result.append(subset1)
            
            dfs(index+1, subset)
            dfs(index+1, subset1)

        dfs(0 , [])

        return result

