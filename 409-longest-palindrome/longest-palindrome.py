class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        h={} 
        t=o=0
        for i in s:
            if i in h:
                h[i]+=1
            else:
                h[i]=1
        
        for k,v in h.items():
            if v % 2 == 1:
                t += 1
        if t >1:
            return len(s) - t+1
        return len(s)
        