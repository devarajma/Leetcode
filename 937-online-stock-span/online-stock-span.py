class StockSpanner(object):

    def __init__(self):
        self.stk =[]
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        if not price:
            return "null"
        span = 1
        if not self.stk:
            self.stk.append((price,span))
            return span

        while self.stk and self.stk[-1][0] <= price:
            p,s = self.stk.pop()
            span+=s
            print(p,s)

        print(span)
        self.stk.append((price,span))
        return span
        
            


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)