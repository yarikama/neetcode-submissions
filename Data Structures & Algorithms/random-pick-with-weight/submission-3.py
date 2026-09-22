import random

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        
        self.n = len(self.w)
        self.prefix = [0] * self.n
        
        prev = 0
        for i in range(self.n):
            self.prefix[i] = prev + self.w[i]
            prev = self.prefix[i] 

    def pickIndex(self) -> int:
        r = random.randint(1, self.prefix[-1])
        L, R = 0, self.n-1

        while L <= R:
            mid = (L + R) // 2
            if self.prefix[mid] < r:
                L = mid + 1
            elif self.prefix[mid] > r:
                R = mid - 1
            else:
                return mid

        return mid



 

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()