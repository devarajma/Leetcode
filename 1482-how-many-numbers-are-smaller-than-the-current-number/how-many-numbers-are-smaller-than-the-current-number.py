class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        h ={}
       
        for i, v in enumerate(sorted(nums)):
            if v not in h:
                h[v]= i
        l = []
        for i in nums:
            l.append(h[i])
        return l
                
                 