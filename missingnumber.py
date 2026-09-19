#LEETCODE 268: FIND THE MISSING NUMBER

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        sumn = (n*(n+1))//2
        return sumn-sum(nums)