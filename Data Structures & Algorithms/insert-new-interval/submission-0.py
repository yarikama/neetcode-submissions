

# 1 3 | 4 6 
#  2  5 
class Solution:
    def insert(
        self, 
        intervals: List[List[int]], 
        newInterval: List[int]
    ) -> List[List[int]]:
        ans = []
        start, end = newInterval

        last_end, last_to_add = 0, True
        for id, itv in enumerate(intervals):
            toAdd = True
            if itv[0] <= start <= itv[1]:
                start = itv[0]
                end = max(end, itv[1])
                toAdd = False
            if itv[0] <= end <= itv[1]:
                end = itv[1]
                start = min(start, itv[0])
                toAdd = False
            if last_end < start and end < itv[0]:
                ans.append([start, end])
            if toAdd:
                if not last_to_add:
                    ans.append([start, end])
                ans.append(itv)  
            last_end = itv[1]
            last_to_add = toAdd

        if not last_to_add:
            ans.append([start, end])

        return ans


            

