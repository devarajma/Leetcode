class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        min_c = [0,0]
        for i in range(2, n+1):
            next_c = min(min_c[i-1] + cost[i-1],
                        min_c[i-2] + cost[i-2])
            min_c.append(next_c)
        return min_c[n]
        