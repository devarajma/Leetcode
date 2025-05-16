class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d ={0:-1}
        sum,r=0,0

        for i in range(len(nums)):
            if nums[i]==1:
                sum+=1
            else:
                sum-=1
            
            if sum in d:
                r = max(r, i-d[sum])
            else:
                d[sum] = i
        
        return r
            
        