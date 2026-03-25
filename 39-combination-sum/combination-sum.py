class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []

        def back(i):
            if sum(sol) == target:
                res.append(sol[:])
                return
            
            if i == len(candidates) or sum(sol) > target:
                return
            
            back(i+1)

            sol.append(candidates[i])
            back(i)
            sol.pop()

        back(0)
        return res   
