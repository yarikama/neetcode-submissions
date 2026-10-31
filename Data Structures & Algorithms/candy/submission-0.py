import heapq

class Solution:
    def candy(self, ratings: List[int]) -> int:
        heap = [(rating, idx) for idx, rating in enumerate(ratings)]
        heapq.heapify(heap)

        candies = [0] * len(ratings)
        while heap:
            rating, idx = heapq.heappop(heap)
            if idx > 0 and ratings[idx] > ratings[idx-1]:
                candies[idx] = max(candies[idx], candies[idx-1] + 1)
            if idx < len(ratings)-1 and ratings[idx] > ratings[idx+1]:
                candies[idx] = max(candies[idx], candies[idx+1] + 1)
            candies[idx] = max(candies[idx], 1)
            print(candies)


        return sum(candies)
