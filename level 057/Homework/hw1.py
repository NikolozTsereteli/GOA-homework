def merge_arrays(arr1, arr2):
    arr1.extend(arr2)
    distinct = []
    for i in arr1:
        if i not in distinct:
            distinct.append(i)
            
    return sorted(distinct)


# ან

def merge_arrays(arr1, arr2):
    return sorted(set(arr1 + arr2))