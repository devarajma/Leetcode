class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        h = {}

        for i in strs:
            s = tuple(sorted(i))

            if s not in h:
                h[s] = []
            h[s].append(i)
        return list(h.values())
        