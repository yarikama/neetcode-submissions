class Solution:
    def search(
        self, 
        nums: List[int], 
        target: int,
    ) -> int:
        # init
        low_id, high_id = 0, len(nums)-1

        # iteration
        while(low_id <= high_id):
            mid_id = (low_id + high_id)//2
            if target < nums[mid_id]:
                high_id = mid_id - 1
            elif target > nums[mid_id]:
                low_id = mid_id + 1
            else:
                return mid_id

        return -1

        