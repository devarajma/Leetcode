class Solution(object):
    def longestConsecutive(self, nums):
        d = set(nums)
        longest = 0

        for i in d:
            if (i-1) not in d:
                length = 1
                while (i+length) in d:
                    length +=1
                longest = max(longest,length)
        return longest