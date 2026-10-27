#LC 974: SUBARRAY SUM DIVISBLE BY K

class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = 0 
        prefix = 0
        freq = {0:1}
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix%k in freq:
                count+=freq[prefix%k]
            freq[prefix%k] = freq.get(prefix%k,0)+1
        return count