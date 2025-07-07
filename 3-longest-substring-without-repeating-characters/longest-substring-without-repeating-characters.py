class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mx = i = 0
        lset = set()

        for j in s:
            while j in lset:
                lset.remove(s[i])
                i+=1
            lset.add(j)
            mx = max(mx,len(lset))
            
        return mx

        