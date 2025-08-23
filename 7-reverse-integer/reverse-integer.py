class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = -1 if x < 0 else 1

        r = int(str(abs(x))[::-1]) * s

        if -2**31 <= r <= 2**31 - 1: 
            return r
        else: return 0
        