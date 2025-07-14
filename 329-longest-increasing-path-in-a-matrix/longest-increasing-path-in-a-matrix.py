class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        ROWS , COLS = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, prev):
            if (r < 0 or r == ROWS or 
                c < 0 or c == COLS or
                matrix[r][c] <= prev):
                return 0

            if (r,c) in dp:
                return dp[(r,c)]

            res = 1
            res = max(res, 1 + dfs(r+1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c+1, matrix[r][c]))
            res = max(res, 1 + dfs(r-1, c, matrix[r][c]))
            res = max(res, 1 + dfs(r, c-1, matrix[r][c]))
            dp[(r,c)] = res
            return res

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, -1)
        return max(dp.values())