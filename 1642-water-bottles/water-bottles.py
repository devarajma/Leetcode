class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        t = numBottles
        while numBottles // numExchange > 0:
            t+=numBottles//numExchange
            numBottles = (numBottles//numExchange) +(numBottles%numExchange)
            print(numBottles)
            
            print(t)
        return t