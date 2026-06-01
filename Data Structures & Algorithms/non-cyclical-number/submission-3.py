class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.get_sum(n)
        while slow != fast:
            fast = self.get_sum(self.get_sum(fast))
            slow = self.get_sum(slow)
        return True if fast == 1 else False

    def get_sum(self, num: int) -> int:
        sum = 0
        while num > 0:
            sum += (num % 10) ** 2
            num //= 10
        return sum


    
