class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        l = len(word)
        for i in range(1,l):
            if word[i-1] != word[i]:
                l-=1
        return l