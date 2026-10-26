#LC 525: CONTIGOUOS SUBARRAY

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        num = [-1 if i == 0 else 1 for i in nums]
        hashmap = {0:-1} 
        prefix = 0 
        max_len = float("-inf")

        for i in range(len(num)):
            prefix += num[i]
            if prefix in hashmap:
                max_len = max(max_len , i-hashmap[prefix])
            else:
                hashmap[prefix] = i
        return max_len if max_len != float("-inf") else 0