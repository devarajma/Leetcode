class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a= []
        max_h= 0
        for i in height:
            if i > max_h:
                max_h = i
            a.append(max_h)
        
        max_h= 0
        b=[]
        for i in height[::-1]:
            if i > max_h:
                max_h = i
            b.append(max_h)
        b.reverse()

        res = 0
        print(a)
        print(b)
        for i in range(len(height)):
            res += (min(a[i],b[i])-height[i])

        return res