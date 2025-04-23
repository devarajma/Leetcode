class Solution(object):
    def isValid(self, s):
        b = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in b:
                stack.append(i)
            elif len(stack) == 0 or b[stack.pop()] != i:
                return False
        return len(stack)== 0
        
        