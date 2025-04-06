class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        c,i=k,1
        n=0
        while c:
            if i not in arr:
                c-=1
                n = i
            i+=1
        return n

        