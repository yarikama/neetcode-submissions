# remember the tail

class Solution:
    def insert(
        self, 
        intervals: List[List[int]], 
        newInterval: List[int]
    ) -> List[List[int]]:

        toInsert = 0
        start, end = newInterval
        skip = set()
        for idx, interval in enumerate(intervals):
            if interval[1] < start:
                toInsert = idx
            if interval[0] <= start <= interval[1]:
                start = interval[0]
                skip.add(idx)
            if interval[0] <= end <= interval[1]:
                end = interval[1]
                skip.add(idx)

        ans = []
        for i in range(len(intervals)):
            if i not in skip:
                ans.append(intervals[i])
            if i == toInsert:
                ans.append([start, end])
        return ans

            

