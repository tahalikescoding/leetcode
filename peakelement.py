#LEETCODE 162: FIND THE PEAK ELEMENT

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l<r:
            m = (l+r)//2
            if nums[m]<nums[m+1]:
                l = m+1
            elif nums[m]>=nums[m+1]:
                r = m 
        return l