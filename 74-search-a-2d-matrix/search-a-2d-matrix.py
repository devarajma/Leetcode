class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        
        rowc = len(matrix)
        colc = len(matrix[0])
        low = 0
        high = (rowc * colc) -1
        

        while low <= high:
            mid = (low+high)//2
            
            r=mid/colc
            c=mid%colc
            val = matrix[r][c]
            print(mid, val)
            if val==target:
                return True
            elif val < target:
                low=mid+1
            else:
                high = mid-1
        return False


        