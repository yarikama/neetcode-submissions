class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points):
            return points

        self.k = k

        self.quick_sort(0, len(points)-1, points)

        return points[:k]

    def quick_sort(self, start: int, end: int, points: List[List[int]]) -> None:
        if start >= end:
            return

        pivot = start
        for i in range(start, end):
            if self.get_distance(points[i]) < self.get_distance(points[end]):
                points[i], points[pivot] = points[pivot], points[i]
                pivot += 1

        points[pivot], points[end] = points[end], points[pivot]
        if pivot == self.k - 1 or \
        self.quick_sort(start, pivot-1, points) == self.k - 1 or \
        self.quick_sort(pivot+1, end, points) == self.k - 1:
            return self.k - 1
        
        return pivot


    def get_distance(self, point: List[int]) -> int:
        return sum(i ** 2 for i in point)
        