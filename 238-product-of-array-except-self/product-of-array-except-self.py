class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = []
        v,p=1,1 
        for i in range(len(nums)):
            if not l:
                l.append(1)
            else:
                v= p * l[i-1]
                l.append(v)
            p=nums[i]
        
    
        p =1
        for i in range(len(nums)-1, -1, -1):
            v= p* l[i]
            l[i] = v
            p *= nums[i]
        
        return l
        