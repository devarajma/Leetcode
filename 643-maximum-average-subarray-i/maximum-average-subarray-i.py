class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        s = sum(nums[:k])
        m = s

        for i in range(k,n):
            s += nums[i]
            s -= nums[i - k]
            m = max(m, s)
        return m/float(k)
        