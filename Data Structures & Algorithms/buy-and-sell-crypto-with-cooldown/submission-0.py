class Solution:
    def maxProfit(
        self, 
        prices: List[int],
    ) -> int:        

        def dfs(i: int, max_profit: int, ableToBuy: bool) -> int:
            if i >= len(prices):
                return max_profit

            if ableToBuy: # Able to Buy
                return max(
                    dfs(i+1, max_profit - prices[i], False), # Buy
                    dfs(i+1, max_profit, True), # Wait
                )
            else:
                return max(
                    dfs(i+2, max_profit + prices[i], True), # Sell
                    dfs(i+i, max_profit, False), # Wait
                )

        return dfs(0, 0, True)


        