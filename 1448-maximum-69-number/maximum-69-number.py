class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        c = num
        n = str(num)
        for i in range(len(n)):
            if n[i] == '6':
                n = n[:i]+ '9'+ n[i+1:]
                break
        return int(n)
        #     print(n)
        #     c = max(int(n),c)
        #     n = str(num)
        # return c

        