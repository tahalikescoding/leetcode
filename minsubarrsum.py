#LEETCODE 209: Minimum Size Subarray Sum

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        total = 0 
        least = float("inf")
        l = 0 
        if not nums:
            return 0
        for r in range(len(nums)):
            total+= nums[r]
            if total>=target:
                while total>=target:
                    least = min(least,r-l+1)
                    total -= nums[l]
                    l+=1           
        return least if least != float("inf") else 0 