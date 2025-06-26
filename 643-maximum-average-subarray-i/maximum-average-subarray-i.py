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
        l,r = 0, k

        while r<n:
            s = s + (nums[r] - nums[l])
            m = max( m, s)
            r+=1
            l+=1

        # for i in range(k,n):
        #     s += nums[i]
        #     s -= nums[i - k]
        #     m = max(m, s)
        return m/float(k)
        