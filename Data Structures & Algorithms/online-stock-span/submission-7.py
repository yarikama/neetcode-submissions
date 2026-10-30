class StockSpanner:

    def __init__(self):
        self.stack = [] # price, swap

    def next(self, price: int) -> int:
        swap = 1

        i = len(self.stack) - 1
        while i >= 0:
            if self.stack[i][0] <= price:
                swap += self.stack[i][1]
                i -= self.stack[i][1]

            else:
                break

        self.stack.append([price, swap])
        return swap
            

        
        

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)