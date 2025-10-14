from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        q = deque()
        q.append((sr,sc))
        m, n= len(image), len(image[0])
        old = image[sr][sc]
        if old == color:
            return image
            
        while q:
            q_l = len(q)
            for _ in range(q_l):
                i,j = q.popleft()
                image[i][j] = color
                for a,b in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0 <= a < m and 0 <= b < n and image[a][b] == old:
                        q.append((a,b))
        return image
        
                        

       