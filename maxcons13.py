#LEETCODE 1004: MAX CONSECUTIVE ONES III

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        z = 0 
        longest = float("-inf")
        l = 0 
        for r in range(len(nums)):
            if nums[r]==0:
                z+=1
            while z>k:
                if nums[l] == 0:
                    z-=1
                l+=1
            longest = max(longest,r-l+1)
        return longest