class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        
        while 1:
            if n == 1:
                return True

            if n in s:
                return False

            s.add(n)
            n = self.get_sum(n)



    def get_sum(self, num: int) -> int:
        sum = 0
        while num > 0:
            sum += int((num % 10)) ** 2
            num /= 10
        return sum


    
