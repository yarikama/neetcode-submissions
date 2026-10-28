from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque(senate)

        cnt = 0
        while q:
            char = q.popleft()
            if char == 'R':
                if cnt >= 0:
                    q.append(char)
                cnt += 1
            else:
                if cnt <= 0:
                    q.append(char)
                cnt -= 1

            if len(q) == cnt:
                return "Radiant"

            if len(q) == -cnt:
                return "Dire"
        