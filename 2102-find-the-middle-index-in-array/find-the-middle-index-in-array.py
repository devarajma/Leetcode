class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls,rs =0,sum(nums)
        for i in range(len(nums)):
            rs -= nums[i]
            if rs == ls:
                return i
            ls+=nums[i]
        return -1