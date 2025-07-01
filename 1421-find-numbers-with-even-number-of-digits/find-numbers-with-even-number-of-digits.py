class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = 0
        for i in nums:
            l =0
            while i:
                i = i // 10
                l+=1
            print(l)
            if not l%2:
                c+=1
        return c