#LEETCODE 238: PRODUCT EXCEPT SELF

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [0]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix*=nums[i]
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            answer[i]*=suffix
            suffix*=nums[i]
        return answer