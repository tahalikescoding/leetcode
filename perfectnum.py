#LEETCODE 507: PERFECT NUMBER

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<0 or num==1:
            return False
        factors = set()
        for i in range(1,int(num**0.5)+1):
            if num%i==0:
                factors.add(i)
                if i!=1:
                    factors.add(num//i)
        return True if sum(factors)==num else False
        


        