class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        R, C = len(coins), amount+1
        cache = []
        for cap in range(C):
            num_coins = cap // coins[0]
            cache.append((num_coins, True if cap % coins[0] == 0 else False))


        for item in range(1, R):
            for cap in range(1, C):
                min_value = float('INF')
                isDivided = True
                for i in range((cap // coins[item]) + 1):
                    if min_value < i + cache[cap - i * coins[item]][0]:
                        continue
                    min_value = i + cache[cap - i * coins[item]][0]
                    isDivided = cache[cap - i * coins[item]][1]
                cache[cap] = (min_value, isDivided)

        return cache[-1][0] if cache[-1][1] else -1
