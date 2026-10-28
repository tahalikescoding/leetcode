#LC 623 CONTINOUS SUBARR SUM

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        good = False
        prefix = 0 
        seen = {0:-1}
        for i in range(len(nums)):
            prefix+=nums[i]
            if prefix%k in seen:
                if i-seen[prefix%k]>=2:
                    good = True
            else:
                seen[prefix%k] = i
        return good