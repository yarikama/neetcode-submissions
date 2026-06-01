class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1] + x[0]))

        rst, curr = 0, 0
        prev_int: List[int] = [-100000, -100000]
        for start, end in intervals:
            if start in range(prev_int[0], prev_int[1]):
                curr += 1
            else:
                curr = 0
            prev_int = [start, end]
            rst = max(curr, rst)

        return rst






        
 
