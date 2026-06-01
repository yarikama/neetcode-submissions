class Solution:
    def maximumProfit(
        self, 
        profit: List[int], 
        weight: List[int], 
        capacity: int
    ) -> int:
        R, C = len(weight), capacity+1
        cache = [[0] * C for _ in range(R)]

        # for c in range(C):
        #     if weight[0] <= c:
        #         # Only one item -> optimized it easily
        #         num_items = c // weight[0]
        #         curr_profit = num_items * profit[0]
        #         cache[0][c] = curr_profit

        # for item in range(1, R):
        for item in range(R):
            for cap in range(1, C):
                skip = cache[item-1][cap]
                include = 0
                if (new_cap := cap - weight[item]) >= 0:
                   include = cache[item][new_cap] + profit[item]
                cache[item][cap] = max(include, skip)

        return cache[-1][-1]





    # def maximumProfit(
    #     self, 
    #     profit: List[int], 
    #     weight: List[int], 
    #     capacity: int
    # ) -> int:
    #     R, C = len(profit), capacity + 1
    #     cache = [[-1] * C for _ in range(R)]

    #     def dfs(i: int, cap: int) -> int:
    #         if i == len(profit): return 0
    #         if cache[i][cap] != -1: return cache[i][cap]

    #         skip = dfs(i+1, cap)
    #         include = 0 if cap - weight[i] < 0 else profit[i] + dfs(i, cap-weight[i])
            
    #         cache[i][cap] = max(skip, include) 
    #         return cache[i][cap]

    #     return dfs(0, capacity)



    # def maximumProfit(
    #     self, 
    #     profit: List[int], 
    #     weight: List[int], 
    #     capacity: int
    # ) -> int:
    #     def dfs(i: int, cap: int) -> int:
    #         if i == len(profit): return 0

    #         skip = dfs(i+1, cap)
    #         include = 0 if cap - weight[i] < 0 else profit[i] + dfs(i, cap-weight[i])
            
    #         return max(skip, include)

    #     return dfs(0, capacity)

