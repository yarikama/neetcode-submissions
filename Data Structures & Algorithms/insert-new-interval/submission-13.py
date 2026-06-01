# remember the tail

class Solution:
    def insert(
        self, 
        intervals: List[List[int]], 
        newInterval: List[int]
    ) -> List[List[int]]:
        res = []
        start_n, end_n = newInterval
        for idx, (start_i, end_i) in enumerate(intervals):
            if start_i > end_n:
                res.append([start_n, end_n])
                return res + intervals[idx:]
            elif end_i < start_n:
                res.append([start_i, end_i])
            else:
                start_n = min(start_n, start_i)
                end_n = max(end_n, end_i)

        res.append((start_n, end_n))
        return res

            

