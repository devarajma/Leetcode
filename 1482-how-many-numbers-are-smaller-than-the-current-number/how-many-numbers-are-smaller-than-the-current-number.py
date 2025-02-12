class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        l =[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count+=1
            l.append(count)
            count =0
        return l        