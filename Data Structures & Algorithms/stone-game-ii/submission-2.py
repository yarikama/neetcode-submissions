"""
Alice & Bob take turns

take all stones in the first X remaining piles.
1 <= X <= 2M 
M = max(M, X) M = 1 initially
until all the stones have been taken
play optimally


Alice M = 1
X = 1
(3, 3 + 1) -> 3 

Bob   M = 1
X = 1
(1, 1 + 2) -> 1

Alice M = 1
X = 2
(2, 2 + 5) -> 7

Bob M = 2
X = 1
(7, 7) -> 7
"""

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        dp = {}

        def dfs(L: int = 0, M: int = 1, is_Alice: bool = True) -> int:
            nonlocal n

            if L >= n:
                return 0, 0

            if (L, M, is_Alice) in dp:
                return dp[(L, M, is_Alice)]

            new_is_Alice = not is_Alice
            
            curr = res_Alice = res_Bob = 0 
            
            for i in range(L, min(n, L + 2*M)):
                curr += piles[i]

                new_res_Alice, new_res_Bob = dfs(i+1, max(M, (i-L+1)), new_is_Alice)

                if is_Alice:
                    if curr + new_res_Alice > res_Alice:
                        res_Alice, res_Bob = (curr + new_res_Alice, new_res_Bob)

                else:
                    if curr + new_res_Bob > res_Bob:
                        res_Alice, res_Bob = (new_res_Alice, curr + new_res_Bob)


            dp[(L, M, is_Alice)] = (res_Alice, res_Bob) 
            return dp[(L, M, is_Alice)]

        return dfs()[0]
















            
        