class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        for i in tokens:
            if i in {"+","-","*","/"}:
                b = stk.pop()
                a = stk.pop()
                if i == "+":
                    stk.append(a+b)
                elif i == "-":
                    stk.append(a - b)
                elif i == "*":
                    stk.append(a * b)
                else:
                    stk.append(int(float(a) / b))
            else:
                stk.append(int(i))
        return stk[-1]