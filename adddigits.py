#LEETCODE 258: ADD DIGITS

class Solution:
    def addDigits(self, num: int) -> int:
        n = num
        if len(str(num))==1:
            return num
        total = 0 
        while n>0:
            n,digit = divmod(n,10)
            total+=digit
        return self.addDigits(total)

test = Solution()
print(test.addDigits(38))