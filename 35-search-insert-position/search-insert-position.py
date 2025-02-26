class Solution(object):
    def searchInsert(self, nums, target):
        for k,v in enumerate(nums):
            if v >= target:
                return k
        return k+1
          
        