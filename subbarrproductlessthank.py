#LC 713 : NUMBER OF SUBARRAY WIT PRODUCT LESS THAN K 

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k<=1:
            return 0
        l = 0 
        prod = 1 
        count = 0 
        for r in range(len(nums)):
            prod *= nums[r]
            while prod>=k:
                prod = prod//nums[l]
                l+=1
            count += r-l+1
        return count