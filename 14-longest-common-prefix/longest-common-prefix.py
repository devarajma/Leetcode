class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        size = len(strs)-1
        strs.sort()
        end = min( len(strs[0]), len(strs[size]) )
        i = 0
        while (i < end and strs[0][i] == strs[size][i]):
            i += 1
        return strs[0][0:i]
