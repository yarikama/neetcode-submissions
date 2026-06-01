class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        times = [(i[0], True) for i in intervals] + [(i[1], False) for i in intervals]
        times.sort()

        sums = []
        cnt, maxCnt = 0, 0
        for _, isStart in times:
            if isStart: cnt += 1
            else: cnt -= 1
            maxCnt = max(cnt, maxCnt)
            if cnt == 0:
                sums.append(maxCnt)

            print(sums)
        
        return sum(max(s - 1, 0) for s in sums)
# 1 2 1 0 -> 1
# s s t t 
# 1 0 1 0 1 0 -> 0
# s t s t s t
# 1 2 3 2 1 0 -> 2
# s s s t t t 
# 1 2 1 2 1 0
# s s t s t t 