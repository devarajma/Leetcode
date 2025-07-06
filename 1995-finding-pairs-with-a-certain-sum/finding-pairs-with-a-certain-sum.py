class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2_count = Counter(nums2)

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.nums2_count[self.nums2[index]] -= 1
        if self.nums2_count[self.nums2[index]] <= 0:
            self.nums2_count.pop(self.nums2[index])

        self.nums2[index] += val
        self.nums2_count[self.nums2[index]] += 1
        

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        c = 0
        # for i in range(len(self.nums2)):
        #     for j in range(len(self.nums1)):
        #         if self.nums1[j]+ self.nums2[i] == tot:
        #             c+=1
        # return c
        for i in self.nums1:
            c += self.nums2_count[tot - i]
        return c

        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)