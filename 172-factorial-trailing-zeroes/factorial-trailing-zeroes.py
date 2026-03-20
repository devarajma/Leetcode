class Solution:
    def trailingZeroes(self, n: int) -> int:
        # def fact(p):
        #     if p == 1 or p == 0:
        #         return 1
        #     return p* fact(p-1)

        # def counting(x):
        #     count = 0
        #     while x > 0:
        #         if x%10 == 0:
        #             count+=1
        #         x //= 10
        # return count  

        # return counting(fact(n)) 
        count = 0
        while n > 0:
            n //= 5
            count +=n
        return count     