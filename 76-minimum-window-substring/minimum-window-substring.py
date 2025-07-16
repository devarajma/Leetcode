class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        i = j = 0
        left = -1
        cht = {}
        formed = 0
        m = float('inf')

        ht = Counter(t) 
        
        while j < len(s):
            cht[s[j]] = cht.get(s[j], 0) + 1

            if s[j] in ht and cht[s[j]] == ht[s[j]]:
                formed += 1

            while formed == len(ht):
                if (j - i + 1) < m:
                    m = j - i + 1
                    left = i

                cht[s[i]] -= 1
                if s[i] in ht and cht[s[i]] < ht[s[i]]:
                    formed -= 1

                i += 1

            j += 1

        return "" if left == -1 else s[left:left + m]