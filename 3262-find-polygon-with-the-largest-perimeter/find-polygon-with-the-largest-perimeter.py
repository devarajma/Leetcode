class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse =True)

        s = sum(nums)
        print(s,nums)
        # for i in range(len(nums)):
        for i in nums:
            # if len(nums) - i ==3:
            #     return s

            s -= i
            print(s,i)
            if s > i:
                return s+i
        return -1
                


        