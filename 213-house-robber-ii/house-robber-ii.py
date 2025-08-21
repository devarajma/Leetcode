class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def check(numss):
            n = len(numss)
            if n == 1: return numss[0]
            if n == 2: return max(numss)

            maxx = [numss[0], max(numss[0], numss[1])]

            for i in range(2, n):
                cur = max(maxx[i-2]+numss[i], maxx[i-1])
                maxx.append(cur)
            return maxx[-1]

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        return max( check(nums[1:]), check(nums[:-1]))
        
