class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m,s = 0,0
        for i in nums:
            s+=i
            m = min(s,m)
        return abs(m)+1
        