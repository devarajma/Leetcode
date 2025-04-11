class Solution(object):
    def countSymmetricIntegers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        c=0
        for i in range(low,high+1):
            if i >10:
                s = str(i)
                l = len(s)//2
                if len(s) %2 ==0:
                    lh= [int(i) for i in s[:l]]
                    rh= [int(i) for i in s[l:]]
                    if sum(lh) ==sum(rh):
                        c+=1
                    
        return c

    
                
        