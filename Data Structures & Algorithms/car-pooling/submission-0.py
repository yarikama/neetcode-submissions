from heapq import heappop, heappush

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        tmp = []
        for num, f, t in trips:
            tmp.append([t, -1 * num])
            tmp.append([f, num])

        tmp.sort()
        print(tmp)
        acc = 0
        for i, num in tmp:
            acc += num
            if acc > capacity:
                print(acc)
                return False

        return True 
            