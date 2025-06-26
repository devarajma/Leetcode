class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        s, trip, tank, n = 0, 0, 0, len(gas)
        for i in range(n):
            trip += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                s = i + 1
                tank = 0
        return s if trip >= 0 else -1

