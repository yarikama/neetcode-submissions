class Solution:
    def twoSum(
        self, 
        nums: List[int], 
        target: int
    ) -> List[int]:
        i, j = 0, len(nums)-1
        nums.sort()
        two_sum = nums[i] + nums[j]
        while two_sum != target:
            if two_sum > target:
                j -= 1
            else:
                i += 1
            print(f"i = {i}, j = {j}")
            two_sum = nums[i] + nums[j]

        return [i, j]


        