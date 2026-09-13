#REVERSING ARRAY USING RECURSION
left = 0 
right = -1
def rev(arr , left = 0 , right = None):
    if right is None:
        right = len(arr)-1
    if left == right:
        return arr 
    arr[left] ,arr[right] = arr[right] , arr[left]
    return rev(arr,left+1,right-1)

print(rev([1,2,3,4,5],1,3))