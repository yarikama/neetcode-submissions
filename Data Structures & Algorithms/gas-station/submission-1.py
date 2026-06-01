class Solution:
    def canCompleteCircuit(
        self, 
        gas: List[int], 
        cost: List[int]
    ) -> int:
        L, R = 0, 0
        tank = gas[R]
        curr_cost = cost[L]
        
        while L < len(gas):
            while tank >= curr_cost:
                tank -= curr_cost
                R += 1
                curr_gas =  gas[R]  if R < len(gas) else gas[R-len(gas)]
                tank += curr_gas
                curr_cost = cost[R] if R < len(gas) else cost[R-len(gas)]
                if R - L == len(gas):
                    return L

            tank -= gas[L]
            tank += cost[L]
            L += 1


        return -1

            



        