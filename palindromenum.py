#LEETCODE Q9 : PALINDROME NUMBER

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        if num<0:
            return False
        result = 0 
        while num>0:
            result *=10
            num,last_digit = divmod(num,10)
            result+=last_digit
        return x==result

        