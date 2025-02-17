class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        ans = []
        min_diff = float('Inf')

        for i in range(len(arr)-1):
            diff = arr[i+1]-arr[i]
            if diff < min_diff:
                min_diff = diff
                ans = [[arr[i], arr[i+1]]]
            elif diff == min_diff:
                ans.append([arr[i], arr[i+1]])
        return ans