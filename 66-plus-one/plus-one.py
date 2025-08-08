class Solution(object):
    def plusOne(self, digits):
        x = int("".join(map(str,digits)))+1
        return [int(d) for d in str(x)]

        