class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """

        def check_score(s, pattern, val):
            stack = []
            score = 0
            for ch in s:
                stack.append(ch)
                if len(stack) >= 2 and stack[-2] + stack[-1] == pattern:
                    stack.pop()
                    stack.pop()
                    score +=val
            return ''.join(stack), score

        if x > y:
            first, second = ("ab",x),("ba",y)
        else:
            first, second = ("ba",y), ("ab",x)

        s, s1 = check_score(s, first[0], first[1])
        _, s2 = check_score(s, second[0], second[1])

        return s1+s2
        # Time Complexity : O(N)
        # Space Complexity: O(N)
        