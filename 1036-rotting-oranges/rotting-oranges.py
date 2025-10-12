from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rotten, fresh, empty = 2,1,0
        num_fresh = 0
        m, n = len(grid), len(grid[0])
        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == fresh:
                    num_fresh += 1
                elif grid[i][j] == rotten:
                    q.append((i,j))
        if num_fresh == 0:
            return 0

        minutes = -1
        while q:
            q_len = len(q)
            minutes += 1
            for _ in range(q_len):
                i, j = q.popleft()
                for r, c in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == fresh:
                        grid[r][c] = rotten
                        num_fresh -= 1
                        q.append((r,c))
        if num_fresh == 0:
            return minutes
        else:
            return -1



        