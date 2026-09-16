def selectionasc(arr):
    for i in range(len(arr)):
        min_idx = i 
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_idx]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr

print(selectionasc([5,7,8,4,1,6,9,2]))

def selectiondesc(arr):
    for i in range(len(arr)):
        max_idx = i 
        for j in range(i+1,len(arr)):
            if arr[j]>arr[max_idx]:
                max_idx = j
        arr[i],arr[max_idx] = arr[max_idx],arr[i]
    return arr

print(selectiondesc([5,7,8,4,1,6,9,2]))

def bubbleasc(arr):
    swap = False
    for i in range(len(arr)-2, -1 ,-1):
        for j in range(i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1] , arr[j]
                swap = True
        if not swap:
            return arr
    return arr

print(bubbleasc([5,7,8,4,1,6,9,2]))


def insertionasc(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1 
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key 
    return arr

print(insertionasc([5,7,8,4,1,6,9,2]))