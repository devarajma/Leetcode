class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 0
        if x < 0:
            x *= -1
            while x:
                r = r*10 + (x%10)
                print(r)
                x = x//10
            r *= -1
        else:
            while x:
                r = r*10 + (x%10)
                print(r)
                x = x//10

        if -2**31 <= r <= 2**31 - 1: 
            return r
        else: return 0
        