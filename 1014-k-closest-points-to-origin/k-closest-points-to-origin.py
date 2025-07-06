class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        p = []
        res = []
 
        
        for i in points:
            x,y = i
            heapq.heappush(p, [sqrt((x*x)+(y*y)), i ])
        
        for _ in range(k):
           a,b =heapq.heappop(p)
           res.append(b) 

        return res