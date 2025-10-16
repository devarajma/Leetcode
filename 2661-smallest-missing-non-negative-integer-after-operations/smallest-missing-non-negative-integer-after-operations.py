class Solution(object):
    def findSmallestInteger(self, nums, value):
        """
        :type nums: List[int]
        :type value: int
        :rtype: int
        """
        # for i in range(len(nums)):
        #     v = nums[i]
        #     if v >= 0 :
        #         while (v - value) >= 0 and (v - value) not in nums:
        #             nums[i] = v - value
        #             v -= value
        #     else:
        #         while (v + value) <= 0 and (v + value) not in nums:
        #             nums[i] = v + value
        #             v += value
        # print(nums)
        # m = 0
        # while m in nums:
        #     m += 1
        # return m
        rem = [0] * value
        for x in nums:
            rem[x % value] += 1
        res = 0
        while rem[res % value]:
            rem[res % value] -= 1
            res += 1
        return res

        