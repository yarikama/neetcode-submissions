from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = [ [q, idx] for idx, q in enumerate(queries) ]

        intervals.sort()
        queries.sort()

        i = 0
        heap, durs = [], []
        for q, idx in queries:
            while i < len(intervals) and intervals[i][0] <= q:
                start_time, end_time = intervals[i]
                heappush(heap, (end_time - start_time + 1, end_time))
                i += 1
            
            res = -1
            while heap:
                dur, end_time = heap[0]
                if end_time < q:
                    heappop(heap)
                else:
                    res = dur
                    break

            durs.append((idx, res))

        durs.sort()
        output = [ res for _, res in durs ]

        return output
            

