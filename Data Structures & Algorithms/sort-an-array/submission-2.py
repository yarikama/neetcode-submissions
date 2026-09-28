class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        stack = [(0, len(nums)-1)]
        while stack:
            s, e = stack.pop()
            if s >= e:
                continue
            p = s
            for i in range(s, e):
                if nums[i] < nums[e]:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
                
            nums[e], nums[p] = nums[p], nums[e]
            stack.append((s, p-1))
            stack.append((p+1, e))
        return nums
        