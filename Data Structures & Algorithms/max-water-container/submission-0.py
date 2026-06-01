class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        cur_volumn, max_volumn = (R - L) * min(heights[R], heights[L]), 0

        while R > L:
            max_volumn = max(cur_volumn, max_volumn)
            if heights[R - 1] > heights[L + 1]:
                R -= 1
            else:
                L += 1
            cur_volumn = (R - L) * min(heights[R], heights[L])

        
        return max_volumn









        