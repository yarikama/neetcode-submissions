class Solution:
    def removeDuplicates(
        self, 
        nums: List[int]
    ) -> int:
        new_nums = [nums[0]]
        for value in nums:
            if value == new_nums[-1]:  
                continue
            else:  
                new_nums.append(value)
        nums[:len(new_nums)] = new_nums
        return len(new_nums)
