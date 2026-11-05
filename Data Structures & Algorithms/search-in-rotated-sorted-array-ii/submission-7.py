class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        L, R = 0, len(nums)-1
        rotated = nums[0] >= nums[-1]          # ← 新增：先判斷整個陣列有沒有旋轉

        while L <= R:
            if nums[L] == target:
                return True

            if nums[L] == nums[R]:
                val = nums[L]
                while nums[L] == val and L < len(nums)-1:
                    L += 1
                while nums[R] == val and R > 0:
                    R -= 1

            mid = (L + R) // 2

            if rotated and (                     # ← 只有真的旋轉時，才做「分段」判斷
                (nums[mid] >= nums[0] and target <= nums[-1])
                or (target >= nums[0] and nums[mid] <= nums[-1])
            ):  # different side
                if nums[mid] > target:
                    L = mid + 1
                elif nums[mid] < target:
                    R = mid - 1
                else:
                    return True
            else:                                # 沒旋轉 or 同一段 → 一般 binary search
                if nums[mid] > target:
                    R = mid - 1
                elif nums[mid] < target:
                    L = mid + 1
                else:
                    return True

        return False