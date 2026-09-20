#LEETCODE 128: LONGEST CONSECUTIVE SEQUENCE

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        best = 0 
        count = 0 
        numset = set(nums)
        for num in numset:
            if num-1 not in numset:
                i = num
                count += 1
                while i+1 in numset:
                    count+=1
                    i+=1
                best = max(count,best)
                count = 0
        return best