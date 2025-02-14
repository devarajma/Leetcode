class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        n = len(arr)
        if len(arr) < 3:
            return 0 

        for i in range(1,len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                l,r=i-1,i+1
                while  l > 0 and arr[l-1] < arr[l]:
                    l-=1
                
                while r < n-1 and arr[r] > arr[r+1]:
                    r+=1
                res = max(res,r-l+1)
        return res if res >= 3 else 0 