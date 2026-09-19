#MERGE TWO SORTED ARRAYS WITHOUT DUPLICATES

def merge_arr(nums1,nums2):
    merged = []
    i = j = 0
    n = len(nums1)
    m = len(nums2)
    while i<n and j<m:
        if nums1[i]<=nums2[j]:
            if nums1[i] not in merged:
                merged.append(nums1[i])
            i+=1
        else:
            if nums2[j] not in merged:
                merged.append(nums2[j])
            j+=1
            
    while i<n:
        if nums1[i] not in merged:
            merged.append(nums1[i])
        i+=1

    while j<m:
        if nums2[j] not in merged:
            merged.append(nums2[j])
        j+=1
    return merged


print(merge_arr([1,1,1],[2,2,2,2,2,2]))