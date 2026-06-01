class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.get_subsets(0, [], result, nums)
        return result

    def get_subsets(
        self, idx: int, cur_subset: List[int], result: List[List[int]], nums: List[int],
    ) -> None:
        # Base Case
        if idx >= len(nums):
            result.append(cur_subset.copy()) # not appending nums[idx]
            return

        cur_subset.append(nums[idx])
        self.get_subsets(idx + 1, cur_subset, result, nums)        
        cur_subset.pop()
        self.get_subsets(idx + 1, cur_subset, result, nums)

        