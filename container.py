#LEETCODE 11: CONTAINER WITH MOST WATER 

class Solution:
    def maxArea(self, height: list[int]) -> int:
        best = 0 
        left = 0 
        area = 0 
        right = len(height)-1
        while left<right:
            area = min(height[left],height[right])*(right-left)
            best = max(area,best)
            if height[left]<=height[right]:
                left+=1
            elif height[right]<=height[left]:
                right-=1
        return best