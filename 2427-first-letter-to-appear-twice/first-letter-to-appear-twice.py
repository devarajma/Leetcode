class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        h = {}
        for i in s:
            if i not in h:
                h[i] = 1
            else:
                return i
        