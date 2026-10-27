#LEETCODE 560: SUBARRAY SUM K

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0 
        freq = {0:1}
        prefix = 0 
        for i in range(len(nums)):
            prefix+=nums[i]
            prev = prefix-k
            if prev in freq:
                count+=freq[prev]
            freq[prefix] = freq.get(prefix,0)+1
        return count