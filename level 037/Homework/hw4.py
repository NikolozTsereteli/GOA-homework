def merge_arrays(arr1, arr2):
    arr1.extend(arr2)
    distinct = []
    for i in arr1:
        if i not in distinct:
            distinct.append(i)
    
    return sorted(distinct)

print(merge_arrays([2, 3, 4, 5, 7], [89, 67, 56, 45, 34, 23]))