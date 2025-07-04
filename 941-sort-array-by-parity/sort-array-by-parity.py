class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = moves = 0
        
        while moves < (len(nums)):
            n = nums[i]
            if n % 2:
                nums.pop(i)
                nums.append(n)
            else:
                i+=1
            moves+=1
                
        return nums 