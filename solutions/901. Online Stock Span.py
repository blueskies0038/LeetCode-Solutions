class StockSpanner:
​
    def __init__(self):
        self.stack = []
        
​
    def next(self, price: int) -> int:
        if self.stack:
            if self.stack[-1][0] > price:
                self.stack.append((price,1))
                return 1
            else:
                count = 1
                while self.stack and self.stack[-1][0] <= price:
                    x,y = self.stack.pop(-1)
                    count += y
                self.stack.append((price,count))
                return count
                
        else:
            self.stack.append((price,1))
            return 1
​
​
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
