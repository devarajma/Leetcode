import math
class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        # max_num = [ -i for i in gifts]
        # heapq.heapify(max_num)
        
        # for _ in range(k):
        #     rich = heapq.heappop(max_num)
        #     num = int(math.sqrt(-rich))
        #     heapq.heappush(max_num, -num)

        # return -sum(max_num)

        # gifts = sorted(gifts, reverse = True)

        for _ in range(k):
            gifts.sort()
            num = gifts.pop()
            r = int(math.sqrt(num))
            gifts.append(r)
        
        return sum(gifts) 