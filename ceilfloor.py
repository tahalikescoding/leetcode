#LARGEST AND SMALLEST NUM IN AN ARRAY

def ceilfloor(nums,target):
    floor = None
    ceil = None
    n = len(nums)
    left = 0
    right = n-1
    while left<=right:
        mid = (left+right)//2
        if nums[mid] == target:
            return [nums[mid],nums[mid]]
        elif nums[mid]>target:
            ceil = nums[mid]
            right = mid-1
        else:
            floor = nums[mid]
            left = mid+1
    return [floor,ceil]
    

print(ceilfloor([3,4,4,4,8,9,9,10,12,12,14,15] , 8))