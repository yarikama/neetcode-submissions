# remember the tail

class Solution:
    def insert(
        self, 
        intervals: List[List[int]], 
        newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals

        toInsert = 0
        # skip = False
        toSkip = set()
        start, end = newInterval
        for idx, interval in enumerate(intervals):
            if interval[1] < start:
                toInsert = idx
            if interval[0] <= start <= interval[1]:
                start = interval[0]
                toSkip.add(idx)
            if interval[0] <= end <= interval[1]:
                end = interval[1]
                toSkip.add(idx)
            if start <= interval[0] and interval[1] < end:
                toSkip.add(idx)

        ans = []
        for i in range(len(intervals)):
            if i not in toSkip:
                ans.append(intervals[i])
            if i == toInsert:
                ans.append([start, end])
        return ans

            

