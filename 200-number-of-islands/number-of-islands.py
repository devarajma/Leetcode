class Solution:
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = [[False]*cols for _ in range(rows)]
        count = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or visited[i][j] or grid[i][j] == '0':
                return
            
            visited[i][j] = True   # FIXED
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:  # FIXED
                    dfs(i, j)
                    count += 1

        return count