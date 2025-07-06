class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = [ -i for i in nums]
        heapq.heapify(arr)

        for _ in range(k):
            val = heapq.heappop(arr)
        
        return -val
        