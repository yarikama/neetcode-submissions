class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # n, m = len(str1), len(str2)
        # dp = {}

        # def dfs(i: int, j: int) -> str:
        #     if i == n:
        #         return str2[j:]

        #     if j == m:
        #         return str1[i:]

        #     if (i, j) in dp:
        #         return dp[(i, j)]

        #     if str1[i] == str2[j]:
        #         res = str1[i] + dfs(i+1, j+1)
        #         dp[(i, j)] = res
        #         return dp[(i, j)]
        #     else:
        #         res1 = dfs(i+1, j)
        #         res2 = dfs(i, j+1)

        #         if len(res1) < len(res2):
        #             res = str1[i] + res1
        #         else:
        #             res = str2[j] + res2

        #         dp[(i, j)] = res
        #         return dp[(i, j)]

        # return dfs(0, 0)

        # n, m = len(str1), len(str2)
        # dp = [["" for _ in range(m+1)] for _ in range(n+1)]
        
        # for i in range(n+1):
        #     dp[i][m] = str1[i:]

        # for j in range(m+1):
        #     dp[n][j] = str2[j:]
        
        # for i in range(n-1, -1, -1):
        #     for j in range(m-1, -1, -1):
        #         if str1[i] == str2[j]:
        #             dp[i][j] = str1[i] + dp[i+1][j+1]
        #         else:
        #             dp[i][j] = str1[i] + dp[i+1][j] if len(dp[i+1][j]) < len(dp[i][j+1]) else str2[j] + dp[i][j+1]

        # return dp[0][0]

        n, m = len(str1), len(str2)
        dp = [str2[j:] for j in range(m+1)]
        
        for i in range(n-1, -1, -1):
            new_dp = ["" for _ in range(m+1)]
            new_dp[m] = str1[i:]
            for j in range(m-1, -1, -1):
                if str1[i] == str2[j]:
                    new_dp[j] = str1[i] + dp[j+1]
                else:
                    new_dp[j] = str1[i] + dp[j] if len(dp[j]) < len(new_dp[j+1]) else str2[j] + new_dp[j+1]
            dp = new_dp

        return dp[0]
         

