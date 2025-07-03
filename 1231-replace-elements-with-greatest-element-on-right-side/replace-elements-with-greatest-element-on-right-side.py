class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        m = -1
        for i in range(len(arr)-1, -1, -1):
            a = arr[i]
            arr[i] = m
            m = max(m, a)
        return arr