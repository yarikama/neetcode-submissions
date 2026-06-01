class Solution:
    def change(
        self, 
        amount: int, 
        coins: List[int],
    ) -> int:
        coins.sort()

        if amount == 0:
            return 1

        def dfs(i: int, amount: int) -> int:
            if i >= len(coins): return 0

            if amount < 0: return 0

            skip = dfs(i+1, amount)

            new_amount = amount - coins[i]

            if new_amount == 0:
                return skip + 1

            return skip + dfs(i, new_amount)

        return dfs(0, amount)















# amount: 1, coin: [1] -> 1
# amount: 2, coin: [1] -> 1
# amount: 3, coin: [1] -> 1
# amount: 4, coin: [1] -> 1
# ...
# amount: 0, coin: [1, 2] -> 1, 0(cache) 
# amount: 1, coin: [1, 2] -> 1, 0(cache) + 1(coin) = 1                          0(cache) = 1
# amount: 2, coin: [1, 2] -> 2, 0(cache) + 2(coin) = 2, 1(cache) + 1(coin) = 2  0(cache) + 1(cache) = 1 + 1 = 2
# amount: 3, coin: [1, 2] -> 2, 1(cache) + 2(coin) = 3, 2(cache) + 1(coin) = 3  1(cache) + 2(cache) = 2 + 1 = 3
# amount: 4, coin: [1, 2] -> 4, 2(cache) + 2(coin) = 4, 3(cache) + 1(coin) = 4  2(cache) + 3(cache) = 2 + 2 = 4

# (1 + 1) + 1
#      2  + 1
# 1 + (1 + 1)

# 5 裡面，所有 coin + cache 的方法，除了一樣的部分。


        