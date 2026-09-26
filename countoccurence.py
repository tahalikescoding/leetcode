def countocc(nums , target):
    n = len(nums)
    lb = 0
    count = 0
    l = 0
    r = n-1
    while l<=r:
        m = (l+r)//2
        if nums[m] == target:
            lb = m 
            r = m-1
        elif nums[m]<target:
            l = m+1
        else:
            r = m-1
    l = lb
    r = n-1
    if not lb:
        return 0
    while l<=r:
        if nums[l] == target:
            count+=1
            l+=1
        elif nums[l] != target:
            break
    return count

print(countocc([1,2,3,3,3,3,3,5,8,9,9,10],9))

