from math import ceil, floor

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        res = [0] * 4
        
        total = sum(matchsticks)
        
        if total % 4 > 0:
            return False
        
        avg = total // 4 

        for m in matchsticks:
            if m > avg:
                return False

        def helper(res: List[int], i: int, avg: int) -> bool:
            if i == len(matchsticks):
                val = res[0]
                for edge in res:
                    if edge != val:
                        return False

                return True

            for edge in range(4):
                if matchsticks[i] + res[edge] > avg:
                    continue

                res[edge] += matchsticks[i]            
                if helper(res, i+1, avg):
                    return True
                res[edge] -= matchsticks[i]

            return False               

        return helper(res, 0, avg)
        