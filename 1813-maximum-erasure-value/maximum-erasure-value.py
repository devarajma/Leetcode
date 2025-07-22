class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        seen = set()
        i, s = 0, 0
        m = float('-inf')
        for n in nums:
            while n in seen:
                s -= nums[i]
                seen.remove(nums[i])
                i += 1
            seen.add(n)
            s += n
            m = max(m, s)
        return m




        