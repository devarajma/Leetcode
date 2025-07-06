class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        p_top = []
        nums = [ [capital[i],profits[i]] for i in range(len(capital))]
        heapq.heapify(nums)

        for _ in range(k) :

            while nums and nums[0][0] <= w:
                c,p = heapq.heappop(nums)
                heapq.heappush(p_top, -p)
            if not p_top:
                break

            w += -heapq.heappop(p_top)

        return w