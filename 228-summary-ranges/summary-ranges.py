class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        i = 0
        res = []
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1] + 1:
                if j - i == 1:
                    res.append("{}".format(nums[i]))
                else:
                    res.append("{}->{}".format(nums[i], nums[j - 1]))
                i = j

        # handle the last range
        if len(nums) - i == 1:
            res.append("{}".format(nums[i]))
        else:
            res.append("{}->{}".format(nums[i], nums[-1]))

        return res