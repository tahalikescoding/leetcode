#LLETCODE 202: HAPPY NUMBER

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        num = n
        total = 0 
        while total!=1:
            total = 0
            while num>0:
                num,last = divmod(num,10)
                total+= last**2
            if total in seen or total == n:
                return False
            seen.add(total)
            num = total
        return True
            
test = Solution()
print(test.isHappy(7))