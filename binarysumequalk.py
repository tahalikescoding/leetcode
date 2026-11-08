class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix = 0 
        freq = {0:1}
        count = 0 
        for i in range(len(nums)):
            prefix+=nums[i]
            if prefix-goal in freq:
                count+=freq[prefix-goal]
            freq[prefix] = freq.get(prefix,0)+1
        return count
        