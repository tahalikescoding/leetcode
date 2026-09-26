#LC 33: SEARCH IN A ROTATED SORTED ARRAY

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[l]<=nums[m]:
                if nums[l]<=target<nums[m]:
                    r = m-1 
                else:
                    l = m+1
            elif nums[r]>=nums[m]:
                if nums[m]<target<=nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1
        