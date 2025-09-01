class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss= []
        tt =[]
        for i in s:
            ss.append(s.index(i))
        for i in t:
            tt.append(t.index(i))

        if ss == tt:
            return True
        else:
            return False
              