#LEETCODE 16 : 3Sum Closest

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        maxsum = float("-inf")
        minsum = float("inf")
        n = len(nums)
        for i in range(0,n):
            if i>0 and nums[i-1]==nums[i]:
                continue
            l = i+1
            r = n-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if s<target:
                    maxsum = max(s,maxsum)
                    l+=1
                elif s>target:
                    minsum = min(s,minsum)
                    r-=1
                else:
                    return s
        return maxsum if abs(maxsum-target)<abs(minsum-target) else minsum
