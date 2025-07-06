class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        original = str(x)
        reverse = original[::-1]

        if original == reverse:
            return True
        return False