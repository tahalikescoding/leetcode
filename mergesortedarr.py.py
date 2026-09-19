#LEETCODE 88: MERGE TWO SORTED ARR

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1 = nums1[:m]
        num2 = nums2
        i = j = 0
        while i < m and j<n:
            if num1[i]<=num2[j]:
                nums1[i+j] = num1[i]
                i+=1
            else:
                nums1[i+j] = num2[j]
                j+=1
        while i < m:
            nums1[i+j] = num1[i]
            i+=1
        while j<n:
            nums1[i+j] = num2[j]
            j+=1
            
