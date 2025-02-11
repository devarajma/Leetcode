class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #simplest
        nums_set = set(nums)  # Convert nums to a set for O(1) lookup
        return [i for i in range(1, len(nums) + 1) if i not in nums_set]