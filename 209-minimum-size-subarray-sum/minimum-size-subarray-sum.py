class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        total=0
        l= 0  
        res = float('inf')
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                res = min(res, i-l+1)
                total-= nums[l]
                l+=1
        if res == float('inf'):
            return 0
        else:
            return res

        