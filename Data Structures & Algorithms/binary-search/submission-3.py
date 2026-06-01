class Solution:
    def search(
        self, 
        nums: List[int], 
        target: int,
    ) -> int:
        L, R = 0, len(nums)-1

        while L <= R:
            mid = (L + R) // 2
            
            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                mid = L - 1
            else:
                mid = R + 1

        return -1
        