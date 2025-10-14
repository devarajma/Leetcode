class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        l = len(flowerbed)

        if not n:
            return True
        for i in range(l):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] ==0) and (i == l-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n-=1
                if not n :
                    return True

        return False

