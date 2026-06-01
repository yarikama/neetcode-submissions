class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()

        if k == 0:
            return False

        for i in range(min(k+1, len(nums))):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])

        print(s)

        for i in range(k+1, len(nums)):
            s.remove(nums[i-(k+1)])
            if nums[i] in s:
                return True
            s.add(nums[i])

        return False
        
        