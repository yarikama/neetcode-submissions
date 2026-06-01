class Solution:
    def maximumProfit(
        self, 
        profit: List[int], 
        weight: List[int], 
        capacity: int,
    ) -> int:
        self.profit, self.weight = profit, weight
        return self.dfs(0, capacity)

    def dfs(self, i: int, capacity: int) -> int:
        # Base Case
        if i == len(self.weight):
            return 0

        # Skip
        maxProfit = self.dfs(i+1, capacity)

        # Retain
        if (newCapacity := capacity - self.weight[i]) >= 0:
            maxProfit = max(maxProfit, self.profit[i] + self.dfs(i+1, newCapacity))

        return maxProfit

