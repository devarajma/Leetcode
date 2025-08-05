class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # mat = []
        # for i in range(m):
        #     mat.append([0] * n)

        # mat[0][0] = 1

        # for i in range(m):
        #     for j in range(n):

        #         if i == 0  and j == 0:
        #             continue
        #         elif i == 0:
        #             mat[i][j] = mat[i][j-1]
        #         else:
        #             mat[i][j] = mat[i][j-1] + mat[i-1][j]
        # return mat[-1][-1]        

        mat = [[1]*n for _ in range(m)]
        

        for i in range(1,m):
            for j in range(1,n):
                mat[i][j] = mat[i][j-1] + mat[i-1][j]
        return mat[-1][-1]