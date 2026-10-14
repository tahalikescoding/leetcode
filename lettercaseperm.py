#LC 764: LETTER CASE PERMUTATION

class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:

        if not s:
            return []
        
        if len(s) == 1:
            return [s,s.upper() if s.islower() else s.lower()] if s.isalpha() else [s]

        res = [""]
        for char in s:
            new_res = []
            for combo in res:
                if char.isalpha():
                    new_res.append(combo+char.lower())
                    new_res.append(combo+char.upper())
                else:
                    new_res.append(combo+char)
            res = new_res
        return new_res