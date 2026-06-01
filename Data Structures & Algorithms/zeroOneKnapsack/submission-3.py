class Solution:
    def maximumProfit(
        self, 
        profit: List[int], 
        weight: List[int], 
        capacity: int,
    ) -> int:
        self.profit, self.weight = profit, weight
        # Create cache! Remember the # of cols here is capacity + 1 not capacity
        R, C = len(weight), capacity + 1
        self.cache = [[-1] * C for _ in range(R)]
        return self.dp(0, capacity)

    def dp(self, i: int, cap: int) -> int:
        # Base Case
        if i == len(self.profit):
            return 0

        # Memorization
        if self.cache[i][cap] != -1:
            return self.cache[i][cap]

        # Skip
        self.cache[i][cap] = self.dp(i+1, cap)

        if (newCap := cap - self.weight[i]) >= 0:
            self.cache[i][cap] = max(self.cache[i][cap], self.profit[i] + self.dp(i+1, newCap))


        return self.cache[i][cap]







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

