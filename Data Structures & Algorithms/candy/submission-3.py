import heapq

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # TC: O(nlogn) SC: O(n)
        # heap = [(rating, idx) for idx, rating in enumerate(ratings)]
        # heapq.heapify(heap)

        # candies = [0] * len(ratings)
        # while heap:
        #     rating, idx = heapq.heappop(heap)
        #     if idx > 0 and ratings[idx] > ratings[idx-1]:
        #         candies[idx] = max(candies[idx], candies[idx-1] + 1)
        #     if idx < len(ratings)-1 and ratings[idx] > ratings[idx+1]:
        #         candies[idx] = max(candies[idx], candies[idx+1] + 1)
        #     candies[idx] = max(candies[idx], 1)

        # return sum(candies)


        # TC: O(n) SC: O(n) 2 pass
        n = len(ratings)
        candies = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)