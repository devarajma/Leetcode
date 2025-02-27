class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
    
        if ''.join(sorted(s.lower())) == ''.join(sorted(t.lower())):
            return True 
        else:
            return False
        
