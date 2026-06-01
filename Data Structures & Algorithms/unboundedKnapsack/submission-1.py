class Solution:
    def maximumProfit(
        self, 
        profit: List[int], 
        weight: List[int], 
        capacity: int
    ) -> int:
        def dfs(i: int, cap: int) -> int:
            if i == len(profit): return 0

            skip = dfs(i+1, cap)
            include = 0 if cap - weight[i] < 0 else profit[i] + dfs(i, cap-weight[i])
            
            return max(skip, include)

        return dfs(0, capacity)

