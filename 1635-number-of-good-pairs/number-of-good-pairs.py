class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c ={}
        res = 0
        for i in nums:
            if i not in c:
                c[i] = 1
            else:
                c[i] += 1

        for k, v in c.items():
            if v > 1:
                res += ((v*(v-1))//2)
        return res

        