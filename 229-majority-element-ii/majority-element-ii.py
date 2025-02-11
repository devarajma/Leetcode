class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d= {}
        n= []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        for k,v in d.items():
            if v > len(nums)/3:
                n.append(k)
        return n

        