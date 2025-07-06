class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [ -i for i in nums]
        heapq.heapify(nums)

        for _ in range(k):
            val = heapq.heappop(nums)

        return -val
        