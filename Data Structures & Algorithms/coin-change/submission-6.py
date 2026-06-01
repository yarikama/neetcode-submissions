class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        R, C = len(coins), amount+1
        cache = []
        for cap in range(C):
            cache.append(cap // coins[0] if cap % coins[0] == 0 else float('INF'))

        for item in range(1, R):
            for cap in range(1, C):
                min_value = float('INF')
                for i in range((cap // coins[item]) + 1):
                    prev = cache[cap - i * coins[item]]
                    if min_value <= i + prev: continue
                    min_value = i + prev
                cache[cap] = min_value

        return cache[-1] if cache[-1] != float('INF') else -1
