from math import ceil, floor

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        side = total // 4

        matchsticks.sort(reverse=True)
        if matchsticks[0] > side:
            return False

        res = [0] * 4

        def helper(i: int) -> bool:
            if i == len(matchsticks):
                return True

            seen = set()
            for edge in range(4):
                if res[edge] in seen or matchsticks[i] + res[edge] > side:
                    continue
                seen.add(res[edge])
            
                res[edge] += matchsticks[i]
                if helper(i+1):
                    return True
                res[edge] -= matchsticks[i]

            return False

        return helper(0)
