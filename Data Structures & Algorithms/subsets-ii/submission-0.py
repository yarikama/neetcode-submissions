class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sorted()
        results = []
        get_subset(
            nums=nums,
            subsets=results
        )
        return 

    def get_subset(
        nums: List[int], 
        idx: int = 0,
        subset: List[int] = list(),
        subsets: List[List[int]] = list(), 
    ) -> None:
        if idx >= len(nums):
            return subset

        subsets.append(nums[idx])
        get_subset(nums, idx+1, subset, subsets)
        subsets.pop(nums[idx])
        while idx < len(nums) and num[idx] == num[idx+1]:
            idx += 1
        get_subset(nums, idx+1, subset, subsets)