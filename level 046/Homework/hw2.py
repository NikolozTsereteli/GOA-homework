def solution(text, ending):
    New_ending = ending[::-1]
    len_ending = len(New_ending)
    if New_ending == text[-1:-(len(ending) + 1):-1]:
        return True
    else:
        return False
    
print(solution("abc", "bc"))