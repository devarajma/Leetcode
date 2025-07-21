class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 3:
            return s
        
        i = 0
        cnt = 1
        res = ""
        res += s[i]
        for j in range(1,len(s)):
            if s[i] == s[j]:
                cnt+=1
                if cnt > 2:
                    continue
            else: 
                cnt = 1
            i = j
            res+=s[i]
        return res

                
            