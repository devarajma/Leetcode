import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in range(len(stones)):
            stones[i] *= -1 

        heapq.heapify(stones)
        while len(stones) > 1:
            w1 = heapq.heappop(stones)
            w2 = heapq.heappop(stones)

            if w1 != w2:
                heapq.heappush(stones, w1 - w2)

        return -heapq.heappop(stones) if stones else 0
        
        