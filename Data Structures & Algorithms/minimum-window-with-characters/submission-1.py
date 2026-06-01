class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        

        t_counter = Counter(t)

        min_L, min_R = 0, len(s)
        L = 0
        for R in range(len(s)):
            if s[R] not in t_counter:
                continue
            
            t_counter[s[R]] -= 1

            while max(t_counter.values()) <= 0:
                if min_R - min_L > R - L:
                    min_R, min_L = R, L
                if s[L] in t_counter:
                    t_counter[s[L]] += 1
                L += 1

        return s[min_L: min_R+1] if min_R - min_L != len(s) else ""