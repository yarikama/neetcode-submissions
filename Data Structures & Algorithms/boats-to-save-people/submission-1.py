class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        lights = []
        for w in people:
            if w == limit:
                res += 1
            else:
                lights.append(w)

        lights.sort()

        L, R = 0, len(lights)-1
        while L <= R:
            if lights[L] + lights[R] <= limit:
                res += 1
                L += 1
                R -= 1

            else:
                res += 1
                R -= 1
                
        return res
