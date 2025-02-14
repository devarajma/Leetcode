class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if len(arr) < 3:
            return 0  # A valid mountain must have at least 3 elements
        
        res = 0
        n = len(arr)
        
        for i in range(1, n - 1):
            if arr[i - 1] < arr[i] > arr[i + 1]:  # Peak condition
                l, r = i, i
                
                while l > 0 and arr[l - 1] < arr[l]:  # Expand left
                    l -= 1
                
                while r < n - 1 and arr[r] > arr[r + 1]:  # Expand right
                    r += 1
                
                res = max(res, r - l + 1)  # Calculate length properly
        
        return res if res >= 3 else 0  # Ensure at least 3 elements in a mountain
