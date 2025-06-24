class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        candies = [1]*n
        count = 0

        for i in range(1, n):
            if ratings[i-1] < ratings[i]:
                candies[i] = candies[i-1]+1

        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                candies[i-1] = max(candies[i]+1, candies[i-1]) 
            count+=candies[i-1]

        return count + candies[n-1]