class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False


        n = len(s)
        good = [False] * n
        good[-1] = True
        cnt = 0
        for i in range(n - 2, -1, -1):
            if i + minJump < n:
                cnt += good[i + minJump]
            if i + maxJump + 1 < n:
                cnt -= good[i + maxJump + 1]
            good[i] = (s[i] == "0" and cnt > 0)
        return good[0]