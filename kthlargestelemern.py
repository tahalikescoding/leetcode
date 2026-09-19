#LEETCODE 215 : KTH LARGEST ELEMENT IN AN ARRAY.

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        def merge_sort(arr):
            if len(arr)<=1:
                return arr
            mid = len(arr)//2
            left_arr = arr[:mid]
            right_arr = arr[mid:]
            left = merge_sort(left_arr)
            right = merge_sort(right_arr)
            merged = []
            i = j = 0 
            while i <len(left) and j<len(right):
                if left[i]<=right[j]:
                    merged.append(left[i])
                    i+=1
                else:
                    merged.append(right[j])
                    j+=1
            if i < len(left):
                merged.extend(left[i:])
            if j < len(right):
                merged.extend(right[j:])
            return merged
        return merge_sort(nums)[-k]




        
        
        