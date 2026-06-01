class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, len(prices)-1

        profit = prices[R] - prices[L]
        while L < R:
            if -prices[R] + prices[R-1] > prices[L] - prices[L+1]:
                R -= 1
            else:
                L += 1
            print(prices[R] - prices[L])
            profit = max(profit, prices[R] - prices[L])

        return max(0, profit)
        