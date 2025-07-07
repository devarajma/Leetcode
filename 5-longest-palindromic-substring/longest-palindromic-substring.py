class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        res = ""
        rlen = 0 
       
        for i in range(len(s)):
            l = r = i
            while 0 <= l and r < len(s) and s[l] == s[r]:
                ln = r - l + 1
                if ln > rlen:
                    rlen = ln 
                    res = s[l:r+1]
                l-=1
                r+=1

        for i in range(len(s)):
            l = i
            r = l+1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                ln = r - l + 1
                if ln > rlen:
                    rlen = ln 
                    res = s[l:r+1]
                l-=1
                r+=1
        return res
                 
        



        
        
            
    