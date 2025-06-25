class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        sign = 1
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit() :
                    num = num * 10 + int(s[i])
                    i+=1
                res += sign * num
                continue
            elif s[i] =='+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append((res, sign))
                res = 0 
                sign = 1
            elif s[i] == ')':
                pres,psign = stack.pop()
                res= res * psign + pres
            i+=1
        return res
        