#LEETCODE 81: SEARCH IN A ROTATED SORTED ARRAY WITH DUPLICATES

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        l = 0 
        r= n-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return True
            while l<r and nums[m] == nums[l] == nums[r]:
                l+=1
            if nums[m]>=nums[l]:
                if nums[l]<=target<nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                if nums[m]<target<=nums[r]:
                    l = m+1
                else:
                    r = m-1
        return False
        