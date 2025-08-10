class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        high = float('-inf')

        cur = 0
        for i in nums:
            cur += i
            high = max(high, cur)
            if cur < 0:
                cur = 0
            
        return high