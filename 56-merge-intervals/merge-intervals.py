class Solution(object):
    def merge(self, intervals):
        res = []
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        fl, fu = intervals[0]
        for i in range(1,len(intervals)):
            sl,su = intervals[i]
            if sl <= fu:
                fu = max(fu, su)
            else:
                res.append([fl,fu])
                fl, fu = sl, su
        
        res.append([fl,fu])
        return res

