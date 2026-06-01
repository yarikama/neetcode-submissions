from copy import deepcopy

class Solution:
    def subsets(
        self, 
        nums: List[int],
    ) -> List[List[int]]:
        result = [[]]
        total_nums = len(nums)

        def dfs(
            index: int = 0, 
            subset: Optional[List[int]] = None,
        ) -> None:
            if index == total_nums:
                return

            subset = subset or []
            subset1 = deepcopy(subset)
            subset1 += [nums[index]]
            result.append(subset1)

            dfs(
                index=index+1,
                subset=subset,
            )
            dfs(
                index=index+1,
                subset=subset1,
            )

            if index == total_nums - 1:
                return


        dfs()

        return result

