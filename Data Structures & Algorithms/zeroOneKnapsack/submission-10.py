class Solution:
    def maximumProfit(
        self, 
        profit: List[int], 
        weight: List[int], 
        capacity: int,
    ) -> int:
        R, C = len(profit), capacity+1
        cache = [0] * C
        for item in range(R):
            for cap in range(C-1, 0, -1): # stop when weight[item] == cap
                if weight[item] > cap:
                    continue
                cache[cap] = max(cache[cap], cache[cap-weight[item]] + profit[item])

        return cache[capacity]

    # def maximumProfit(
    #     self, 
    #     profit: List[int], 
    #     weight: List[int], 
    #     capacity: int,
    # ) -> int:
    #     R, C = len(profit), capacity + 1
    #     cache = [[0] * C for _ in range(R)]

    #     # 0 Capacity means no way to gain profix
    #     # for i in range(R):
    #         # cache[i][0] = 0

    #     # Start from the very beginning
    #     for cap in range(C):
    #         if cap >= weight[0]:
    #             cache[0][cap] = profit[0]


    #         for cap in range(C):
    #             skip = cache[item-1][cap]
    #             retain = profit[item] + cache[item-1][cap-weight[item]] if cap-weight[item] >= 0 else 0
    #             cache[item][cap] = max(skip, retain)

    #     return cache[R-1][C-1]










    # def maximumProfit(
    #     self, 
    #     profit: List[int], 
    #     weight: List[int], 
    #     capacity: int,
    # ) -> int:
    #     self.profit, self.weight = profit, weight
    #     # Create cache! Remember the # of cols here is capacity + 1 not capacity
    #     R, C = len(weight), capacity + 1
    #     self.cache = [[-1] * C for _ in range(R)]
    #     return self.dp(0, capacity)

    # def dp(self, i: int, cap: int) -> int:
    #     # Base Case
    #     if i == len(self.profit):
    #         return 0

    #     # Memorization
    #     if self.cache[i][cap] != -1:
    #         return self.cache[i][cap]

    #     # Skip
    #     self.cache[i][cap] = self.dp(i+1, cap)

    #     # Retain
    #     if (newCap := cap - self.weight[i]) >= 0:
    #         self.cache[i][cap] = max(self.cache[i][cap], self.profit[i] + self.dp(i+1, newCap))

    #     return self.cache[i][cap]






    # def maximumProfit(
    #     self, 
    #     profit: List[int], 
    #     weight: List[int], 
    #     capacity: int,
    # ) -> int:
    #     self.profit, self.weight = profit, weight
    #     return self.dfs(0, capacity)

    # def dfs(self, i: int, capacity: int) -> int:
    #     # Base Case
    #     if i == len(self.weight):
    #         return 0

    #     # Skip
    #     maxProfit = self.dfs(i+1, capacity)

    #     # Retain
    #     if (newCapacity := capacity - self.weight[i]) >= 0:
    #     # Can't write like '''if newCapacity := capacity - self.weight[i] >= 0:'''
    #         maxProfit = max(maxProfit, self.profit[i] + self.dfs(i+1, newCapacity))

    #     return maxProfit

