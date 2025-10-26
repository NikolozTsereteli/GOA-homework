def check_exam(arr1,arr2):
    score = 0
    for i in range(0, len(arr1)):
        if arr1[i] == arr2[i]:
            score += 4
        elif arr1[i] != arr2[i] and arr2[i] != "":
            score -=1
    if score < 0:
        return 0
    
    return score

print(check_exam([1, 2, 3, 4], [1, 3, 5, 4]))