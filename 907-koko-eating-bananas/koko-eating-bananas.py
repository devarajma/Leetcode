class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        l = 1
        u = max(piles)
        while l <= u:
            n = 0
            mid = (l + u) // 2
    
            for i in piles:
                n += ( i + mid - 1 ) // mid
                
            print(mid, n)
            if n <= h:
                u = mid - 1
            else:
                l = mid + 1    
        return l
