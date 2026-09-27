#LEETCODE 643: MAXIMUM AVERAGE SUBARRAY 1

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l = 0 
        total = 0 
        best = float("-inf")
        if not nums:
            return 0
        for r in range(len(nums)):
            if (r-l) == k:
                best = max(best,total)
                total -= nums[l]
                l+=1 
            total += nums[r]
        return max(total,best)/k