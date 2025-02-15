class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        s={}

        for i in range(len(nums)):
            if nums[i] in s and abs(i - s[nums[i]]) <= k:
                return True
            s[nums[i]] = i
        return False
        
        