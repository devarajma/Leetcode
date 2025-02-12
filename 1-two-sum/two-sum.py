class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}

        for i, v in enumerate(nums):
            d = target - v
            if d in h:
                return [h[d],i]
            h[v] = i