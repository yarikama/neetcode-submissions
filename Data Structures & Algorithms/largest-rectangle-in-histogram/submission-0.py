class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0, -1)] # val, start_len
        max_area = 0
        heights.append(0)
        for idx, val in enumerate(heights):
            if stack[-1][0] < val:
                stack.append((val, idx))
                continue

            idx_start = idx
            while stack[-1][0] > val:
                val_start, idx_start = stack.pop()
                area = (idx - idx_start) * val_start
                # print(stack, area)
                max_area = max(area, max_area)

            stack.append((val, idx_start))

        return max_area
            
        
# 小於 前一個 -> stopped and record this one and start a new one
# 大於 前一個 -> start a new one