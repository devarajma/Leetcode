class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:


        rows, cols = len(image), len(image[0])
        iclr = image[sr][sc]

        def dfs(i, j):
            if i >= rows or j >= cols or i < 0 or j < 0 or image[i][j] != iclr:
                return 
            if image[i][j] == iclr:
                image[i][j] = color
            if iclr == color:
                return image
            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i-1, j)


        dfs(sr, sc)

        return image
        