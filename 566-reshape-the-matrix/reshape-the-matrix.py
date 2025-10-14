class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m , n = len(mat), len(mat[0])

        if m*n == r*c: 
            l = []
            for i in mat:
                l.extend(i)
            g =[]
            j = 0
            for i in range(r):
                g.append(l[j:j+c])
                j = j+c
            return g

        else:
            return mat
        
                