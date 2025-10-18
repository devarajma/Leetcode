class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = 0 
        st = [-1]   
        for k, v in enumerate(s):
            if v == "(":
                st.append(k)
            else:
                st.pop()
                if not st:
                    st.append(k)
                else:
                    c = max(c, k- st[-1])
        return c
                