#LEETCODE 17: Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        buttons = {
            "1":None,
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"        
        }
        if len(digits) == 1:
            return list(buttons[digits])
        
        res = [""]
        for digit in digits:
            new_res = []
            for i in res:
                for letter in buttons[digit]:
                    new_res.append(i+letter)
            res = new_res
        
        return res
            