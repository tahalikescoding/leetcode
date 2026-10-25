#LC 39: COMBINATION SUM

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def dectree(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i>=len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dectree(i , cur , total + candidates[i])
            cur.pop()
            dectree(i+1,cur,total)
        
        dectree(0,[],0)
        return res