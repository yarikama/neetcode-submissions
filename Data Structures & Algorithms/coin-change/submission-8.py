class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        R, C = len(coins), amount+1
        cache = []
        for cap in range(C):
            cache.append(cap // coins[0] if cap % coins[0] == 0 else float('INF'))

        for item in range(1, R):
            for cap in range(1, C):
                cache[cap] = min(cache[cap], 1 + cache[cap - coins[item]] if cap - coins[item] >= 0 else float('INF')) 

        return cache[-1] if cache[-1] != float('INF') else -1
