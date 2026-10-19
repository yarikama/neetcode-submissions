from heapq import heappop, heappush

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        tmp = []
        for num, f, t in trips:
            tmp.append([t, -1 * num])
            tmp.append([f, num])

        tmp.sort()
        acc = 0
        for i, num in tmp:
            acc += num
            if acc > capacity:
                return False

        return True 
            