class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        times = [(interval[0],  True) for interval in intervals]
        times += [(interval[1], False) for interval in intervals]  
        times.sort(key=lambda x: (x[0], -x[1]))

        ans = []
        stack_cnt = 0
        L, R = 0, 0
        for time, is_start in times:
            if stack_cnt == 0:
                if is_start:
                    L = time
                else:
                    R = time
                    ans.append([L, R])

            if is_start:
                stack_cnt += 1
            else: 
                stack_cnt -= 1

            if stack_cnt == 0:
                if is_start:
                    L = time
                else:
                    R = time
                    ans.append([L, R])

        return ans
        