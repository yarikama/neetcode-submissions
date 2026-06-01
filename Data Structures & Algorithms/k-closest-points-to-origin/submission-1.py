import heapq


class Solution:
    def kClosest(
        self, 
        points: List[List[int]], 
        k: int
    ) -> List[List[int]]:
        self.heap = []
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            heapq.heappush(self.heap, (distance, point))

        return [result[1] for result in heapq.nsmallest(k, self.heap)] 