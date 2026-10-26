class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # edge cases for the first and the last one
        # only can buy for the beginning
        # only can sell in the end
        # consider for plateau

        new_prices = [prices[0]]
        for p in prices:
            if p != new_prices[-1]:
                new_prices.append(p)
        prices = new_prices

        prev = float("inf")
        prices.append(float("-inf"))

        total, curr = 0, 0
        for i in range(len(prices)-1):
            if prev < prices[i] and prices[i] > prices[i+1]:
                profit = prices[i] - curr
                total += profit

            if prev > prices[i] and prices[i] < prices[i+1]:
                curr = prices[i]

            prev = prices[i] 

        return total

        