class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        
        swap = 0
        for i in range(len(self.stack)-1, -1, -1):
            if price >= self.stack[i]:
                swap += 1
            else:
                return swap
                
        return swap
        

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)