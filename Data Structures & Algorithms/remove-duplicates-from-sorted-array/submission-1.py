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
        print(nums)
        print(new_nums)
        nums = new_nums
        print(nums)
        return len(new_nums)
