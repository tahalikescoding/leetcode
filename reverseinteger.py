#LEET CODE Q7 REVERSE AN INTEGER

class Solution:
    def reverse(self, x: int) -> int:
        result = 0 
        num = abs(x)
        while num>0:
            result*=10
            num,last_digit = divmod(num,10)
            result += last_digit
        if (result< -2**31 or result > (2**31)-1):
            return 0
        elif x>=0:
            return result
        elif x<0:
            return -result