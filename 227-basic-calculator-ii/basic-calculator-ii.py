class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        op = '+'
        i = 0 
        num = 0 
        res= 0
        p = 0

        while i < n:
            if s[i].isdigit():
                while i < n and s[i].isdigit():
                    num = num*10 + int(s[i])
                    i+=1
                i-=1
            
                if op == '+':
                    res+= num
                    p = num
                elif op =='-':
                    res+= -num
                    p = -num
                elif op =='*':
                    res -= p
                    p = p* num
                    res += p 
                else:
                    res -= p
                    p = int(float(p) / num) 
                    res += p
                num = 0

            elif s[i] != " ":
                op = s[i]

            i+=1
        return res

        # n = len(s)
        # op = '+'
        # i = 0 
        # num = 0 
        # res = 0
        # p = 0  # \U0001f527 initialized for * and /

        # while i < n:
        #     if s[i].isdigit():
        #         num = 0
        #         while i < n and s[i].isdigit():
        #             num = num * 10 + int(s[i])
        #             i += 1
        #         i -= 1  # \U0001f527 prevent skipping next char

        #         if op == '+':
        #             res += num
        #             p = num
        #         elif op == '-':
        #             res -= num
        #             p = -num
        #         elif op == '*':
        #             res -= p
        #             p = p * num
        #             res += p
        #         elif op == '/':
        #             res -= p
        #             p = int(float(p) / num)  # \U0001f527 int() for truncation
        #             res += p
        #         num = 0  # \U0001f527 reset after use

        #     elif s[i] != " ":
        #         op = s[i]

        #     i += 1
        # return res