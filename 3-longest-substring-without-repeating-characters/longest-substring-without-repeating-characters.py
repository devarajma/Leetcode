class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = m = 0
        l = set()
        
        for j in range(len(s)):
            while s[j] in l:
                l.remove(s[i])
                i+=1
            l.add(s[j])
            m = max(m, j-i+1)
        return m
        