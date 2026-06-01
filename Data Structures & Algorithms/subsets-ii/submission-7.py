class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        self.get_subset(
            nums,
            0,
            list(),
            results
        )
        return results

    def get_subset(
        self,
        nums: List[int], 
        idx: int = 0,
        subset: List[int] = list(),
        subsets: List[List[int]] = list(), 
    ) -> None:
        if idx >= len(nums):
            return subset

        subsets.append(nums[idx])
        self.get_subset(nums, idx+1, subset, subsets)
        subsets.pop(nums[idx])
        while idx < len(nums) and nums[idx] == numß[idx+1]:
            idx += 1
        self.get_subset(nums, idx+1, subset, subsets)