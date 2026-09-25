#LEETCODE 34: FIND THE FIRST AND LAST POSITON OF AN ELEMENT IN AN ARRAY

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = -1
        end = len(nums)
        n = len(nums)
        l = 0 
        r = n-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                start = m 
                r = m-1
            elif nums[m]>target:
                r = m-1
            elif nums[m]<target:
                l = m+1
        if start == -1:
            return [-1,-1]
        l = 0 
        r = n-1
        while l<=r:
            m = (l+r)//2
            if nums[m]>target:
                end = m
                r = m-1
            else:
                l = m+1
        return [start,end-1]