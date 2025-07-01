class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        for i in tokens:
            if i == "+":
                stk.append(stk.pop()+stk.pop())
            elif i =="-":
                n = stk.pop()
                stk.append(stk.pop()-n)
            elif i=="*":
                stk.append(stk.pop() *stk.pop())
            elif i=="/":
                n = stk.pop()
                stk.append(int(float(stk.pop()) / n))
            else:
                stk.append(int(i))
        return stk[-1]