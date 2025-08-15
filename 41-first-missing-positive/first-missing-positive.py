class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [n for n in nums if n > 0]

        nums.sort()

        t = 1
        for i in nums:
            if i == t:
                t+=1
        return t
            
                
        