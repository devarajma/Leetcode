class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        rs,ls,count = sum(nums), 0, 0
        for num in nums[:-1]:
            rs-=num
            ls+=num
            if ls >= rs:
                count+=1
            
        return count