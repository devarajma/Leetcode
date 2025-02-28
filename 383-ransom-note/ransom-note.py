class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dic ={}

        for char in magazine:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] +=1
        
        for char in ransomNote:
            if char in dic and dic[char] > 0:
                dic[char] -= 1
            else:
                return False
        return True
        






        # s = ransomNote.lower()
        # t = magazine.lower()
        # if len(s) == len(t):
        #     sorts = sorted(s)
        #     sortt = sorted(t)
        #     if sortt == sorts:
        #         return True
        #     else:
        #         return False
        # else:
        #     return False