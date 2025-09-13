def capitals(word):
    New_list = []
    for i in range(len(word)):
        if word[i].upper() == word[i]:
            New_list.append(i)
    
    return New_list

print(capitals("CodEWaRs"))