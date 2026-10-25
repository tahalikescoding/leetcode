#LC 42: TRAPPING RAIN WATER 

class Solution:
    def trap(self, height: list[int]) -> int:
        highest = height.index(max(height))
        maxcur = 0 
        water = 0

        for cur in range(0,highest):
            if height[cur]<maxcur:
                water += maxcur-height[cur]
                continue
            maxcur = height[cur]
        
        maxcur = 0 

        for cur in range(len(height)-1,highest , -1):
            if height[cur]<maxcur:
                water += maxcur-height[cur]
                continue
            maxcur = height[cur]
        
        return water