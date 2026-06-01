from copy import deepcopy

class Solution:
    def combinationSum(
        self, 
        nums: List[int], 
        target: int
    ) -> List[List[int]]:
        self.nums = nums
        self.result = []
        self.nums_count = len(nums)
        self.dfs(target)
        return self.result

    def dfs(
        self,
        target: int,
        index: int = 0,
        subset: Optional[List[int]] = None,
        use_last: bool = False
    ) -> None:
        if index > len(self.nums) - 1:
            return

        target -= self.nums[index]
        subset = subset or []
        new_subset = deepcopy(subset)
        new_subset.append(self.nums[index])

        if target < 0:
            return

        if target == 0:
            self.result.append(new_subset)
            return
        
        # not choose
        if not use_last:
            self.dfs(
                target=target+self.nums[index],
                index=index+1,
                subset=subset,
            )

        #choose
        for i in range(index, len(self.nums)):
            self.dfs(
                target=target,
                index=i,
                subset=new_subset,
                use_last=True,
            )



