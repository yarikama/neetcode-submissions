class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        times = [(i[0], True) for i in intervals] + [(i[1], False) for i in intervals]
        times.sort()

        cnt, maxCnt = 0, 0
        for _, isStart in intervals:
            if isStart: cnt += 1
            else: cnt -= 1
            maxCnt = max(cnt, maxCnt)

        return maxCnt - 2

        