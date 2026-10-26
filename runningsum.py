#LC 1480: RUNNING SUM OF 1D ARRAY

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = []
        run = 0 
        for i in range(len(nums)):
            run += nums[i]
            result.append(run)
        return result
