class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        s = 0
        while i < len(nums) and nums[i]== nums[i-1]+1:
            s+= nums[i-1]
            i+=1

        s+=nums[i-1]
        while s in nums:
            s+=1
        return s

        