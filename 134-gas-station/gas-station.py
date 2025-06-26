class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas)<sum(cost):
            return -1

        s, tank, n = 0, 0, len(gas)
        for i in range(n):
            tank += gas[i] - cost[i]
            if tank < 0:
                s = i + 1
                tank = 0
        return s 

