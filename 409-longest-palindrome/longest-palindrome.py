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
            print(k,v)
            t += v//2
            o+=v%2
        
        return 2*t+(1 if o > 0 else 0)
        