class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            k-= 1- nums[j]
            if k < 0:
                k += 1 - nums[i]
                i += 1
        return j - i + 1
        
        