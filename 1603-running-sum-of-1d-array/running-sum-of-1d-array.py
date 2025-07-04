class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = 0 
        res = []
        for i in nums:
            s += i
            res.append(s)
        return res