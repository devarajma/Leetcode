class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p,n = 1,nums[0]
        for i in range(1,len(nums)):
            if p==0:
                n = nums[i]
                p+=1
            elif nums[i]==n:
                p+=1
            else:
                p-=1
        return n