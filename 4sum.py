#LEETCODE 18: 4SUM

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for i in range(0,n):
            if i>0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1,n):
                if j>i+1 and nums[j-1] == nums[j]:
                    continue
                l = j+1
                r = n-1
                while l<r:
                    s = nums[i]+nums[j]+nums[l]+nums[r]
                    if s>target:
                        r-=1
                    elif s<target:
                        l+=1
                    else:
                        result.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while l<r and nums[l-1] == nums[l]:
                            l+=1
                        while l<r and nums[r+1] == nums[r]:
                            r-=1
        return result
        