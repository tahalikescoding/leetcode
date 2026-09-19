#LEETCODE 53: MAX SUBARRAY

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        total = 0
        best = float("-inf")
        for i in nums:
            total+=i
            best = max(total,best)
            if total<0:
                total = 0 
        return best