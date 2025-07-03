class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        m = 10**9+7
        l , r , res= 0, len(nums)-1, 0
        power = [1] * len(nums)
        for i in range(1, len(nums)):
            power[i] = (power[i - 1] * 2) % m
        while l <= r:
            if nums[l]+ nums[r] <= target:
                res = (res + power[r-l]) % m
                l+=1
            else:
                r-=1
        return res