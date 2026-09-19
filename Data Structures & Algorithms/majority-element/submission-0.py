class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        prev, cnt = 0, 0
        for num in nums:
            if cnt == 0:
                prev = num

            if prev == num:
                cnt += 1
            else:
                cnt -= 1

        return prev


        