#LEETCODE 485: MAX CONSECUTIVE ONES

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0 
        best = 0 
        for num in nums:
            if num:
                count+=1
            if not num:
                best = max(count,best)
                count = 0 

        return max(best,count)

        