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
            # 後面那段了 -> append new 然後直接把尾巴加進來
            if start_i > end_n:
                res.append([start_n, end_n])
                return res + intervals[idx:]
            # 前面那段，res 不停加入 ith item
            elif end_i < start_n:
                res.append([start_i, end_i])
            # 中間，持續 merge
            else:
                start_n = min(start_n, start_i)
                end_n = max(end_n, end_i)

        res.append((start_n, end_n))
        return res

            

