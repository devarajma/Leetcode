from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        word = Counter(text)
        
        b_count = word['b']
        a_count = word['a']
        l_count = word['l'] // 2
        o_count = word['o'] // 2
        n_count = word['n']

        return min(b_count, a_count, l_count, o_count, n_count)        