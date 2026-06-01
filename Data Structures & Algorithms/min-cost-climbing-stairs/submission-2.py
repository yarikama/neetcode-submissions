class Solution:
    def minCostClimbingStairs(
        self, 
        cost: List[int],
    ) -> int:
        if len(cost) <= 2: return min(cost)

        prev, curr = cost[-1], cost[-2]

        for i in range(len(cost) - 3, -1, -1):
            tmp = cost[i] + min(prev, curr)
            prev = curr
            curr = tmp

        return min(prev, curr)


