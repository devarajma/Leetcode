class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        s = sorted(heights)
        print(s)
        c = 0
        for i in range(len(s)):
            if s[i] != heights[i]:
                c += 1
        return c