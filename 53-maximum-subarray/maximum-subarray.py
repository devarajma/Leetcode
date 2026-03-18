class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m_sum = float('-inf')
        c_sum = 0

        for i in nums:
            c_sum = c_sum+i
            if c_sum > m_sum:
                m_sum = c_sum
            if c_sum < 0:
                c_sum = 0
        return m_sum