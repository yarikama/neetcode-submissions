class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_day = days[-1]
        travels = set(days)
        n = last_day + 1
        dp = [0] * n
        
        for i in range(1, n):
            if i not in travels:
                dp[i] = dp[i-1]
                continue

            dp[i] = min(
                dp[i-1] + costs[0], 
                dp[max(0, i-7)] + costs[1], 
                dp[max(0, i-30)] + costs[2]
            )

        return dp[-1]