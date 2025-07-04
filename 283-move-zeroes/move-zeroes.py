class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
       
        for i in range(len(nums)):
            if nums[i]!=0:
                if i != j:
                    nums[j] = nums[i]
                    nums[i] = 0
                j+=1