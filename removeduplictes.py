#LEETCODE 26:REMOVE DUPLICTES FROM SORTED ARRAY

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        k = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k] = nums[i]
                k+=1
        return k