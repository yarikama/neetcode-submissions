class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        # for i in range(k):
        #     prev = nums[i]
        #     nxt = i + k
        #     while nxt < n + k:
        #         nums[nxt % n], prev = prev, nums[nxt % n]
        #         nxt += k
        #     print(nums)

        for i in range(k):
            prev = nums[-1]
            for j in range(len(nums)):
                nums[j], prev = prev, nums[j]

