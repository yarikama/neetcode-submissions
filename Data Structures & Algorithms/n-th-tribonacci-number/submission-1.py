from collections import deque

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        q = deque([0, 1, 1])
        for i in range(2, n):
            q.append(sum(q))
            q.popleft()

        return q[-1]
        