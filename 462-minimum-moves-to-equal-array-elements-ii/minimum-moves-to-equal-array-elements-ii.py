class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        nums.sort()
        med = nums[len(nums)//2]
        for i in nums:
            c += abs(med - i)
        return c
        