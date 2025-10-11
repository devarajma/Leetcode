class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j):
            
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0
                
            else:
                grid[i][j] = 0
                return 1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j+1) + dfs(i,j-1)

        
        m, n = len(grid), len(grid[0])
        mx_a = 0        

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    mx_a = max(dfs(i,j),mx_a)
        return mx_a



        