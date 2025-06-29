class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1 =nums1+nums2
        nums1.sort()
        mid = len(nums1)//2
        md = (nums1[mid] + nums1[~mid]) /2.0
        return md