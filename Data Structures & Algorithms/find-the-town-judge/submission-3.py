class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_to = [set() for _ in range(n+1)]

        max_num = 0
        max_to = -1
        for fr, to in trust:
            trust_to[to].add(fr)
            num = len(trust_to[to])
            if max_num < num:
                max_num = num
                max_to = to

        if max_to == -1:
            return -1

        if max_num != n-1:
            return -1

        for trust_set in trust_to:
            if max_to in trust_set:
                return -1

        return max_to