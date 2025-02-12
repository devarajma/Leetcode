class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x1, y1 = points.pop()
        res= 0
        while points:
            x2, y2 = points.pop()
            res+=max(abs(y1-y2),abs(x1-x2))
            x1,y1 = x2,y2
        
        return res

    