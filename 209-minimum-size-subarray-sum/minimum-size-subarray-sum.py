class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # tot = 0
        # res = float('inf')
        # l = 0 
        # for i in range(len(nums)):
        #     tot +=nums[i]
        #     while tot >= target:
        #         res = min(res, i-l+1)
        #         tot-= nums[l]
        #         l+=1
        
        # if res == float('inf'):
        #     return 0
        # else:
        #     return res

        i = j = s =0
        res = float('inf')
        while j <len(nums):
            s += nums[j]
            while s >= target:
                res = min(res, j-i+1)
                s-=nums[i]
                i+=1
            j+=1

        if res == float('inf'):
            return 0
        else:
            return res

