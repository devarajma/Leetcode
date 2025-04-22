class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # rs,ls,count = sum(nums),0,0
        # if rs and len(nums) > 2:
        #     for i in range(len(nums)):
        #         if ls >= rs:
        #             count+=1
        #         rs-=nums[i]
        #         ls+=nums[i]
        # return count

        rs,ls,count = sum(nums)-nums[0],nums[0],0
        for i in range(1,len(nums)):
            print(ls,rs)
            if ls >= rs:
                count+=1
            rs-=nums[i]
            ls+=nums[i]
        return count