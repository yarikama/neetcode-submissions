class Solution:
    def removeElement(
        self, 
        nums: List[int], 
        val: int
    ) -> int:
        nums_removed_val = []
        for i in nums:
            if i != val:
                nums_removed_val.append(i)
        k = len(nums_removed_val)
        nums = nums_removed_val
        return k
        