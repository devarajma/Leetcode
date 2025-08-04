class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        dic = collections.defaultdict(int)

        l = res = total = 0

        for r in range(len(fruits)):
            dic[fruits[r]]+=1
            total+=1

            while len(dic) > 2:
                dic[fruits[l]]-=1
                total-=1
                if not dic[fruits[l]]:
                    dic.pop(fruits[l])
                l+=1
            res = max(res,total)
        return res
