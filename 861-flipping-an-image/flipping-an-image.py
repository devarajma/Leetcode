class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """

        m, n = len(image),len(image[0])

        for i in range(m):
            image[i] = image[i][::-1]
            image[i] = [1- x for x in image[i]]
        return image