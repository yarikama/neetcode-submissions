class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights)-1
        max_volumn = 0
        while R > L:
            cur_volumn = (R - L) * min(heights[R], heights[L])
            max_volumn = max(cur_volumn, max_volumn)

            if heights[R] > heights[L]:
                L += 1
            else:
                R -= 1

        return max_volumn








        