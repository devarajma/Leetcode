class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = 0
        l =[]
        i,j =0,1
  
        while i <len(nums):
            if nums[j] < nums[i]:
                    count+=1
            j+=1
            if j==len(nums):
                l.append(count)
                i,j,count=i+1,0,0
        return l 
                
                 