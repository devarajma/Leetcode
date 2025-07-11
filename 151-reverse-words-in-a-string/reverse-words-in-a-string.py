class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()[::-1]
        res = ""
        j = i = 0
        while i < len(s):
            if s[i] == " " :
                res += s[j:i][::-1]

                while i+1 < len(s) and s[i+1] == " ":
                    i+=1
                j = i+1
                res+=" "

            if i == len(s)-1:
                res += s[j:][::-1]
            i+=1

        return res

                