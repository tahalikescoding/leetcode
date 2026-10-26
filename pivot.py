#LC 724: FIND PIVOT INDEX

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        suml = 0
        for i in range(len(nums)):
            sumr = total-nums[i]-suml
            if sumr == suml:
                return i 
            suml+=nums[i]
        return -1