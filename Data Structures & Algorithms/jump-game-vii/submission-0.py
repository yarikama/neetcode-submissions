class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False

        s = list(s)

        for i in range(len(s)-2, -1, -1):
            if s[i] == "1":
                continue
            
            s[i] = "1"
            for j in range(minJump, maxJump + 1):
                if i+j < len(s) and s[i+j] == "0":
                    s[i] = "0"
                    break


        return s[0] == "0"