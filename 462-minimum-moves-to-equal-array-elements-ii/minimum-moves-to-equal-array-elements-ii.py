class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        nums.sort()
        avg = len(nums)//2
        if len(nums)%2:
            med = nums[avg]
        else:
            med = ( nums[avg] + nums[avg - 1]) //2

        for i in nums:
            c += abs(med - i)
        return c
        