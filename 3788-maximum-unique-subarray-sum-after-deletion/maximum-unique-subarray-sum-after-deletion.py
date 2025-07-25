class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)

        nums = list(nums)
        nums.sort(reverse = True)

        mx = float('-inf')
        s = 0
        prev = nums[0]
        for i in nums:
            if s+i < prev:
                return mx
            s+=i
            if s > mx:
                mx  = s
                prev = s
        return mx

        