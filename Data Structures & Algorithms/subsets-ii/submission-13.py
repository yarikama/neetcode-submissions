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
            subsets.append(subset.copy())
            return

        subset.append(nums[idx])
        self.get_subset(nums, idx+1, subset, subsets)

        subset.pop()
        while idx+1 < len(nums) and nums[idx] == nums[idx+1]:
            idx += 1

        self.get_subset(nums, idx+1, subset, subsets)