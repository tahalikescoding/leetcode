#LC 153: FIND THE MINIMUM IN ROTATED SORTED ARRAY

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        l = 0 
        r = n-1
        min_element = float("inf")
        while l<=r:
            m = (l+r)//2
            if nums[m]>=nums[l]:
                min_element = min(min_element,nums[l])
                l = m+1 
            elif nums[m]<=nums[r]:
                min_element = min(min_element,nums[m])
                r = m-1
        return min_element

        