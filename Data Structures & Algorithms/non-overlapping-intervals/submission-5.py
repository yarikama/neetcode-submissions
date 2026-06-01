class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        curr_end = -50000
        rst = 0
        for start, end in intervals:
            if start < curr_end:
                rst += 1
            else:
                curr_end = end

        return rst