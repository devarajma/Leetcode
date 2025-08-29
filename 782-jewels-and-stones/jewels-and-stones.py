class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels = set(jewels)
        res = 0
        for s in stones:
            if s in jewels:
                res+=1
        return res
        