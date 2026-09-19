#LEETCODE 2149: REARRANGE ELEMENTS BY SIGN

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        result = [0]*len(nums)
        i = 0
        j = 1
        for num in nums:
            if i<len(nums) and num>0:
                result[i] = num
                i+=2
            if j<len(nums) and num<0:
                result[j] = num
                j+=2
        return result
