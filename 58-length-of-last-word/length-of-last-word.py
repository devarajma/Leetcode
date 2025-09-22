class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        print(words)  
        if not words:
            return 0
        return len(words[-1])      