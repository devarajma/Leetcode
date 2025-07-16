class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        odd = even = both =0

        c = nums[0] % 2
        for i in nums:
            if i % 2:
                odd+=1
            else:
                even+=1
            if i%2 == c:
                both += 1
                c = 1 - c
        return max(both, even, odd)        