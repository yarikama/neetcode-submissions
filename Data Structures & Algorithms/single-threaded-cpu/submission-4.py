from heapq import heappop, heappush

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [
            (eq_time, pro_time, idx) 
            for idx, (eq_time, pro_time) 
            in enumerate(tasks)
        ]
        tasks.sort()

        res = []
        heap = [] 
        i = time = 0
        while i < len(tasks):
            if not heap:
                eq_time, pro_time, idx = tasks[i]
                heap = [[pro_time, idx, eq_time]]
                time = eq_time # ********
                i += 1

            while heap:
                pro_time, idx, eq_time = heappop(heap)
                res.append(idx)
                time += pro_time # *******

                while i < len(tasks):
                    eq_time1, pro_time1, idx1 = tasks[i]
                    if time >= eq_time1:
                        heappush(heap, [pro_time1, idx1, eq_time1])
                        i += 1
                    else:
                        break

        return res