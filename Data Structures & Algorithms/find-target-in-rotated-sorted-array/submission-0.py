class Solution:
    def search(self, nums: List[int], target: int) -> int:
        is_first = True if target > nums[0] else False

        L, R = 0, len(nums)-1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] == target:
                return mid
            if is_first:
                if nums[mid] < nums[0]:
                    R = mid - 1
                elif nums[mid] < target:
                    L = mid + 1
                elif nums[mid] > target:
                    R = mid - 1
            else:
                if nums[mid] > nums[-1]:
                    L = mid + 1
                elif nums[mid] < target:
                    L = mid + 1
                elif nums[mid] > target:
                    R = mid - 1

        return -1