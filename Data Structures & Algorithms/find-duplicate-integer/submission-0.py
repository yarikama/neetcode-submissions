class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slower1, slow, fast = 0, 0, 0
        
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if slow == fast:
                break

        while slower1 != slow:
            slower1 = nums[slower1]
            slow = nums[slow]

        return slow