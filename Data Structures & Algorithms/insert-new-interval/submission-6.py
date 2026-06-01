# remember the tail

class Solution:
    def insert(
        self, 
        intervals: List[List[int]], 
        newInterval: List[int]
    ) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        toInsert = 0
        skip = False
        toSkip = set()
        start, end = newInterval
        for idx, interval in enumerate(intervals):
            if interval[1] < start:
                toInsert = idx
            if interval[0] <= start <= interval[1]:
                start = interval[0]
                skip = True
            if interval[0] <= end <= interval[1]:
                end = interval[1]
                skip = True
            if interval[0] > end:
                skip = False

            if skip:
                toSkip.add(idx)

        ans = []
        for i in range(len(intervals)):
            if i not in toSkip:
                ans.append(intervals[i])
            if i == toInsert:
                ans.append([start, end])
        return ans

            

