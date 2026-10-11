#LEETCODE 1299 : Replace Elements with Greatest Element on Right Side

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        leader = -1
        for i in range(len(arr)-1,-1,-1):
            num = arr[i]
            arr[i] = leader
            if num>=leader:
                leader = num
        return arr