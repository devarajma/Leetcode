class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result = 0
        number = 0
        sign = 1  
        
        for c in s:
            if c.isdigit():
                number = number * 10 + int(c)
            elif c in "+-":
                result += sign * number
                number = 0
                sign = 1 if c == '+' else -1
            elif c == '(':

                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif c == ')':
                result += sign * number
                number = 0
                result *= stack.pop() 
                result += stack.pop()  
        
        result += sign * number
        return result
