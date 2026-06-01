class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()

        if k == 0:
            return False

        for i in range(k+1):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])

        for i in range(k+1, len(nums)):
            s.remove(nums[i-(k+1)])
            if nums[i] in s:
                return True

        return False
        
        