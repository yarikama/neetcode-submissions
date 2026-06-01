class Solution:
    def combinationSum(
        self, 
        nums: List[int], 
        target: int
    ) -> List[List[int]]:
        self.nums = nums
        self.result = []
        self.dfs(target)
        return self.result

    def dfs(
        self,
        target: int,
        choosen_num: int = 0,
        subset: Optional[List[int]] = None,
    ) -> None:
        subset = subset or []

        target -= choosen_num
        if target < 0:
            return

        new_subset = subset.copy()
        if choosen_num != 0:
            new_subset.append(choosen_num)

        if target == 0:
            self.result.append(new_subset)
            return

        for i in self.nums:
            if target < i:
                break
            
            if choosen_num > i:
                continue

            self.dfs(
                target=target,
                choosen_num=i,
                subset=new_subset
            )
        

        