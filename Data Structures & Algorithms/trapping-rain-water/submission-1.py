class Solution:
    def trap(self, height: List[int]) -> int:
        L, R = 0, len(height)-1
        h_l, h_r  = height[L], height[R]
        result = 0
        while L < R:
            if h_r < h_l:
                R -= 1

                if height[R] > h_r:
                    h_r = height[R]
                else:
                    result += h_r - height[R]

            else:
                L += 1

                if height[L] > h_l:
                    h_l = height[L]
                else:
                    result += h_l - height[L]

        return result
        