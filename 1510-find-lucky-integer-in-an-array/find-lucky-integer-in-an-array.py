class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        h = dict()
        for i in arr:
            if i in h :
                h[i] +=1
            else:
                h[i] = 1
            
        num = [ i for i in h if i == h[i] ]
        if num:
            return num[-1]
        
        return -1
        