def minimum(arr):
    min = arr[0]
    for i in arr:
        if i < min:
            min = i
    return min

print(minimum([1, 2, 3, 4, 5]))
        

def maximum(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max

print(maximum([1, 2, 3, 4, 5]))