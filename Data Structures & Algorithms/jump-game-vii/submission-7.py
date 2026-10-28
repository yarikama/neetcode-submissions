class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        good = [False] * n
        good[-1] = s[-1] == "0"
        cnt = 0
        for i in range(n - 2, -1, -1):
            if i + minJump < n:
                cnt += good[i + minJump]
            if i + maxJump + 1 < n:
                cnt -= good[i + maxJump + 1]
            good[i] = s[i] == "0" and cnt > 0
        return good[0]