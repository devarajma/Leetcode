class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        d =[]
        for i in arr:
            if i*2 in d or (i//2 in d and i%2==0):
                return True
            d.append(i)
        return False
        