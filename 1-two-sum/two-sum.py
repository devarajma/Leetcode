class Solution(object):
    def twoSum(self, nums, target):
        checked={}
        for k, v in enumerate(nums):
            a = target-v
            if a in checked:
                return [checked[a], k]
            checked[v] = k