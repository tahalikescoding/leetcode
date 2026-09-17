def piv(nums,low,high):
    pivot = nums[low]
    i = low
    j = high
    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1
        while nums[j]>=pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i],nums[j] = nums[j],nums[i]
    nums[low],nums[j] = nums[j],nums[low]
    return j

def quick_sort(arr,low,high):
    if low<high:
        p = piv(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)

arr = [4,1,7,6,3,2,8]
quick_sort(arr,0,6)
print(arr)