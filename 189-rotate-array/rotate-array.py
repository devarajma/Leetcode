class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = n - (k%n)
        nums[:k]= nums[:k][::-1]
        nums[k:]= nums[k:][::-1]
        nums[:]= nums[::-1]
            