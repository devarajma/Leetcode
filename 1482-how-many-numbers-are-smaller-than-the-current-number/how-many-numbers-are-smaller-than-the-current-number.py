class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        h ={}
        a = sorted(nums)
        for i, v in enumerate(a):
            if v not in h:
                h[v]= i
        l = []
        for i in nums:
            l.append(h[i])
        return l
                
                 